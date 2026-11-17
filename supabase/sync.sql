-- ISLGrind cross-device sync: progress saved online under a sync code.
-- Run once in the Supabase dashboard (SQL Editor → paste → Run). Safe to run again.
--
-- One row per sync code. Only the code's SHA-256 is stored, never the code itself.
-- Row-level security is on with no policies, so the site's public key can reach the
-- table only through the three functions below. Anyone holding a code can read and
-- replace that code's progress, and nothing else.

create table if not exists public.isl_sync (
  code_hash  text primary key,
  rev        bigint      not null,
  data       jsonb       not null,
  updated_at timestamptz not null default now()
);
alter table public.isl_sync enable row level security;
revoke all on table public.isl_sync from anon, authenticated;

-- a 12-character code (Crockford base-32, no dashes) → its row key; null if malformed
create or replace function public.isl_sync_key(p_code text) returns text
language sql immutable set search_path = pg_catalog as $$
  select case when p_code ~ '^[0-9A-HJKMNP-TV-Z]{12}$'
              then encode(sha256(convert_to(p_code, 'UTF8')), 'hex') end
$$;

-- start syncing: store a device's progress under a new code
-- → {ok:true, rev:1}, or {ok:false} if that code is already in use
create or replace function public.isl_sync_create(p_code text, p_data jsonb) returns jsonb
language plpgsql security definer set search_path = public, pg_catalog as $$
declare k text := isl_sync_key(p_code);
begin
  if k is null then raise exception 'invalid sync code'; end if;
  if octet_length(p_data::text) > 4000000 then raise exception 'progress too large to sync'; end if;
  insert into isl_sync(code_hash, rev, data) values (k, 1, p_data) on conflict (code_hash) do nothing;
  if not found then return jsonb_build_object('ok', false); end if;
  return jsonb_build_object('ok', true, 'rev', 1);
end $$;

-- read a code's progress → null if the code is unknown;
-- just {rev} when the caller already has that revision, else {rev, data}
create or replace function public.isl_sync_pull(p_code text, p_have bigint default 0) returns jsonb
language sql stable security definer set search_path = public, pg_catalog as $$
  select case when s.rev = p_have then jsonb_build_object('rev', s.rev)
              else jsonb_build_object('rev', s.rev, 'data', s.data) end
  from isl_sync s
  where s.code_hash = isl_sync_key(p_code)
$$;

-- save a new copy, only on top of the revision the device last saw
-- → {ok:true, rev}; another device saved first → {ok:false, rev, data} (the current copy,
--   to combine and retry); unknown code → {ok:false}
create or replace function public.isl_sync_push(p_code text, p_data jsonb, p_base bigint) returns jsonb
language plpgsql security definer set search_path = public, pg_catalog as $$
declare k text := isl_sync_key(p_code); r public.isl_sync;
begin
  if k is null then raise exception 'invalid sync code'; end if;
  if octet_length(p_data::text) > 4000000 then raise exception 'progress too large to sync'; end if;
  update isl_sync set rev = rev + 1, data = p_data, updated_at = now()
    where code_hash = k and rev = p_base
    returning * into r;
  if found then return jsonb_build_object('ok', true, 'rev', r.rev); end if;
  select * into r from isl_sync where code_hash = k;
  if not found then return jsonb_build_object('ok', false); end if;
  return jsonb_build_object('ok', false, 'rev', r.rev, 'data', r.data);
end $$;

revoke all on function public.isl_sync_key(text) from public, anon, authenticated;
revoke all on function public.isl_sync_create(text, jsonb) from public;
revoke all on function public.isl_sync_pull(text, bigint) from public;
revoke all on function public.isl_sync_push(text, jsonb, bigint) from public;
grant execute on function public.isl_sync_create(text, jsonb) to anon, authenticated;
grant execute on function public.isl_sync_pull(text, bigint) to anon, authenticated;
grant execute on function public.isl_sync_push(text, jsonb, bigint) to anon, authenticated;

notify pgrst, 'reload schema';
