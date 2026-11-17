const assert = require('node:assert/strict');
const { readFileSync } = require('node:fs');
const { join } = require('node:path');
const { test } = require('node:test');
const vm = require('node:vm');

const root = join(__dirname, '..');
const html = readFileSync(join(root, 'index.html'), 'utf8');

function section(start, end) {
  const from = html.indexOf(start);
  const to = html.indexOf(end, from);
  assert.ok(from >= 0 && to > from, `Cannot find application section: ${start}`);
  return html.slice(from, to);
}

// The application's own sync section; only storage keys and the browser crypto are supplied.
const PKEY = 'isl_trainer_profiles_v1';
const SKEY = id => `isl_trainer_state_v1:${id}`;
const app = vm.createContext({ PKEY, SKEY, crypto: globalThis.crypto, lsGet: () => null });
vm.runInContext(section('/* ---------- sync across devices', '/* ===== adaptive engine'), app);

const three = [{ id: 'p1', name: 'Leon' }, { id: 'p2', name: 'Sheldon' }, { id: 'p3', name: 'Annabel' }];
const progress = (m, extra = {}) => JSON.stringify({ ...(m ? { _m: m } : {}), solved: {}, attempts: [], ...extra });
function copy(states, { profiles = three, active = 'p1', listM } = {}) {
  const d = { _app: 'islgrind', _v: 1, _t: 0,
    [PKEY]: JSON.stringify({ profiles, active, ...(listM ? { _m: listM } : {}) }) };
  for (const [id, s] of Object.entries(states)) d[SKEY(id)] = s;
  return d;
}
const agreedOn = d => ({ local: app.dumpPrints(d), cloud: app.dumpPrints(d) });
const merge = (local, cloud, base) => app.syncMerge(local, cloud, base);
const listOf = d => JSON.parse(d[PKEY]);

const before = copy({ p1: progress(100), p2: progress(100), p3: progress(100) });

test('a profile changed on one device only takes that device\'s copy, whatever the clocks say', () => {
  const local = { ...before, [SKEY('p1')]: progress(50, { solved: { A1: true } }) };   // earlier stamp than the base
  assert.equal(merge(local, before, agreedOn(before))[SKEY('p1')], local[SKEY('p1')]);
  const cloud = { ...before, [SKEY('p1')]: progress(50, { solved: { C1: true } }) };
  const later = { ...before, [SKEY('p1')]: before[SKEY('p1')] };
  assert.equal(merge(later, cloud, agreedOn(before))[SKEY('p1')], cloud[SKEY('p1')]);
});

test('different profiles changed on different devices are both kept', () => {
  const local = { ...before, [SKEY('p1')]: progress(300, { solved: { A1: true } }) };
  const cloud = { ...before, [SKEY('p2')]: progress(200, { solved: { G2: true } }) };
  const merged = merge(local, cloud, agreedOn(before));
  assert.equal(merged[SKEY('p1')], local[SKEY('p1')]);
  assert.equal(merged[SKEY('p2')], cloud[SKEY('p2')]);
  assert.equal(merged[SKEY('p3')], before[SKEY('p3')]);
});

test('a profile changed on both devices keeps the later change', () => {
  const early = progress(200, { solved: { A1: true } }), late = progress(201, { solved: { N4: true } });
  assert.equal(merge({ ...before, [SKEY('p1')]: late }, { ...before, [SKEY('p1')]: early }, agreedOn(before))[SKEY('p1')], late);
  assert.equal(merge({ ...before, [SKEY('p1')]: early }, { ...before, [SKEY('p1')]: late }, agreedOn(before))[SKEY('p1')], late);
});

test('entering a code on a device with no shared history keeps the later change per profile', () => {
  const untouched = copy({ p1: progress(0), p2: progress(0), p3: progress(500, { solved: { C3: true } }) });
  const synced = copy({ p1: progress(300, { solved: { A1: true } }), p2: progress(0), p3: progress(400) });
  const merged = merge(untouched, synced, null);
  assert.equal(merged[SKEY('p1')], synced[SKEY('p1')]);    // the fresh device never touched it
  assert.equal(merged[SKEY('p2')], synced[SKEY('p2')]);    // neither did: the synced copy is kept on a tie
  assert.equal(merged[SKEY('p3')], untouched[SKEY('p3')]); // practised here more recently
  // copies saved before profiles carried a change time fall back to their latest attempt
  const old = copy({ p1: progress(0, { attempts: [{ t: 900, ok: true }] }) });
  assert.equal(merge(old, synced, null)[SKEY('p1')], old[SKEY('p1')]);
});

test('profile list: an added profile arrives with its progress; changed on both, the later list wins', () => {
  const four = [...three, { id: 'p4', name: 'Kate' }];
  const added = copy({ ...Object.fromEntries(three.map(p => [p.id, before[SKEY(p.id)]])), p4: progress(700) },
    { profiles: four, listM: 700 });
  const merged = merge(before, added, agreedOn(before));
  assert.deepEqual(listOf(merged).profiles.map(p => p.name), ['Leon', 'Sheldon', 'Annabel', 'Kate']);
  assert.equal(merged[SKEY('p4')], added[SKEY('p4')]);

  const renamed = copy({ p1: progress(100), p2: progress(100), p3: progress(100) },
    { profiles: [{ id: 'p1', name: 'Leo' }, ...three.slice(1)], listM: 900 });
  assert.deepEqual(listOf(merge(added, renamed, agreedOn(before))).profiles.map(p => p.name), ['Leo', 'Sheldon', 'Annabel']);
  assert.deepEqual(listOf(merge(renamed, added, agreedOn(before))).profiles.map(p => p.name), ['Leo', 'Sheldon', 'Annabel']);
});

test('the profile open on each device stays that device\'s choice', () => {
  const onSheldon = copy({ p1: progress(100), p2: progress(100), p3: progress(100) }, { active: 'p2' });
  const cloud = { ...before, [SKEY('p1')]: progress(150, { solved: { A1: true } }) };
  assert.equal(listOf(merge(onSheldon, cloud, agreedOn(onSheldon))).active, 'p2');
  // a deleted open profile falls back to the first remaining one
  const deleted = copy({ p1: progress(100), p3: progress(100) }, { profiles: [three[0], three[2]], listM: 999 });
  assert.equal(listOf(merge(onSheldon, deleted, agreedOn(onSheldon))).active, 'p1');
});

test('an unusable synced copy never replaces this device\'s progress', () => {
  const local = { ...before, [SKEY('p1')]: progress(150) };
  for (const bad of [null, { _app: 'other' }, { _app: 'islgrind', [PKEY]: '{"profiles":[]}' }, { _app: 'islgrind', [PKEY]: 'x' }]) {
    assert.equal(merge(local, bad, agreedOn(before)), local);
  }
});

test('sync codes: 12 unambiguous characters, typed in any reasonable form', () => {
  for (let i = 0; i < 200; i++) assert.match(app.newSyncCode(), /^[0-9A-HJKMNP-TV-Z]{12}$/);
  assert.equal(vm.runInContext('fmtCode', app)('K7QF2M9XHR4T'), 'K7QF-2M9X-HR4T');
  for (const typed of ['K7QF-2M9X-HR4T', 'k7qf 2m9x hr4t', ' k7qf2m9xhr4t ']) assert.equal(app.normCode(typed), 'K7QF2M9XHR4T');
  assert.equal(app.normCode('OILO-0000-0000'), '011000000000');   // O read as 0, I and L as 1
  for (const bad of ['', 'K7QF-2M9X-HR4', 'K7QF-2M9X-HR4TT', 'K7QF-2M9X-HR4U', null]) assert.equal(app.normCode(bad), null);
});
