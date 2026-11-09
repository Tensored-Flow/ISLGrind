const assert = require('node:assert/strict');
const { readFileSync } = require('node:fs');
const { join } = require('node:path');
const { test } = require('node:test');
const vm = require('node:vm');

const root = join(__dirname, '..');
const html = readFileSync(join(root, 'index.html'), 'utf8');
const context = vm.createContext({ window: {} });
// Load exactly the bank scripts shipped by the application, in their real order.
for (const [, file] of html.matchAll(/<script src="(bank[^"/]*\.js)"><\/script>/g)) {
  vm.runInContext(readFileSync(join(root, file), 'utf8'), context, { filename: file });
}
const bank = Array.from(context.window.ISL_BANK);
const apmo = bank.filter(p => p.source === 'APMO');

function section(start, end) {
  const from = html.indexOf(start);
  const to = html.indexOf(end, from);
  assert.ok(from >= 0 && to > from);
  return html.slice(from, to);
}

test('APMO ships all official papers, 1989–2026, with exactly P1–P5 per year', () => {
  assert.equal(apmo.length, 190);
  assert.equal(bank.length, 1944);
  assert.equal(new Set(bank.map(p => p.id)).size, bank.length);
  for (let year = 1989; year <= 2026; year++) {
    const paper = apmo.filter(p => p.year === year);
    assert.deepEqual(paper.map(p => p.number), [1, 2, 3, 4, 5]);
    assert.deepEqual(paper.map(p => p.code), ['P1', 'P2', 'P3', 'P4', 'P5']);
    for (const p of paper) {
      assert.equal(p.url, `https://www.apmo-official.org/static/problems/apmo${year}_prb.pdf`);
      assert.equal(p.format, 'latex');
      assert.ok(p.body.trim());
      assert.doesNotMatch(p.body, /\b(?:Answer|Solution)\s*:/i);
    }
  }
});

test('all 124 old APMO IDs remain usable by progress, notes, boards and gyms', () => {
  for (const [topic, count] of Object.entries({ A: 37, C: 20, G: 45, N: 22 })) {
    for (let number = 1; number <= count; number++) {
      assert.equal(apmo.filter(p => p.id === `APMO-${topic}${number}`).length, 1);
    }
  }
  // These records were out of chronological order or ambiguous under text matching.
  for (const [id, year, number] of [
    ['APMO-A1', 2006, 1], ['APMO-A2', 1989, 1], ['APMO-A5', 1991, 3],
    ['APMO-A21', 2007, 4], ['APMO-G45', 2024, 5], ['APMO-N22', 2025, 5],
  ]) {
    const p = apmo.find(p => p.id === id);
    assert.equal(p.year, year);
    assert.equal(p.number, number);
  }
});

test('the application displays official year/number labels and links', () => {
  const app = vm.createContext({});
  vm.runInContext(section('function srcName(p)', 'function fillMath('), app);
  const p = apmo.find(p => p.year === 2025 && p.number === 2);
  assert.equal(app.probRef(p), 'APMO 2025 · P2');
  assert.equal(app.aopsLink(p), p.url);
  assert.equal(app.problemLinkLabel(p), 'official');
  assert.match(app.srcHTML(p, true), /APMO 2025 · P2/);
  assert.match(app.srcHTML(p, true), /apmo2025_prb\.pdf/);
  assert.doesNotMatch(app.srcHTML(p, false), /2025|P2/); // existing reveal behavior
});

test('Browse finds APMO by year/number and saved legacy progress still resolves', () => {
  const app = vm.createContext({
    BANK: bank,
    state: { solved: { 'APMO-A2': true }, review: { 'APMO-N22': true },
      notes: { 'APMO-A2': 'My notes' }, gyms: [{ ids: ['APMO-A2'] }] },
  });
  vm.runInContext(section('function srcName(p)', '// pill colour') +
    section('function hasNote(id)', '/* shared scoring core') +
    section('let dbQ=""', 'function renderDB(){'), app);
  vm.runInContext('dbSrc="APMO"; dbQ="P2 2026";', app);
  assert.deepEqual(Array.from(app.dbMatches(), p => p.id), ['APMO-2026-2']);
  vm.runInContext('dbQ=""; dbStat="solved";', app);
  assert.deepEqual(Array.from(app.dbMatches(), p => p.year), [1989]);
  vm.runInContext('dbStat="review";', app);
  assert.deepEqual(Array.from(app.dbMatches(), p => p.year), [2025]);
  for (const status of ['noted', 'gym']) {
    vm.runInContext(`dbStat="${status}";`, app);
    assert.deepEqual(Array.from(app.dbMatches(), p => p.id), ['APMO-A2']);
  }
});

test('official statements correct legacy answer leaks and preserve fragile formulas', () => {
  const at = (year, number) => apmo.find(p => p.year === year && p.number === number).body;
  assert.doesNotMatch(at(1998, 4), /ABC'/);
  assert.match(at(1995, 1), /2\\sqrt\{a_n-\(n-1\)\}/);
  assert.match(at(2000, 5), /a_\{i-1\}\+1=a_j/);
  assert.match(at(2013, 2), /\\frac\{n\^2\+1\}\{\\lfloor\\sqrt n\\rfloor\^2\+2\}/);
  assert.match(at(2026, 1), /m\^o\+26/);
  assert.match(at(2026, 2), /A_\{2\^n\}/);
});

test('loading, saving and exporting four profiles preserves their full solve histories', () => {
  const profileKey = 'isl_trainer_profiles_v1';
  const stateKey = id => `isl_trainer_state_v1:${id}`;
  const profiles = ['p1', 'p2', 'p3', 'p4'].map(id => ({ id, name: `Profile ${id}` }));
  const manifest = { active: 'p1', profiles };
  const storage = new Map([[profileKey, JSON.stringify(manifest)]]);
  const subjects = ['Algebra', 'Combinatorics', 'Geometry', 'Number Theory'];
  const app = vm.createContext({
    SUBJECTS: subjects, PM: manifest, PKEY: profileKey, SKEY: stateKey,
    MKEY: 'isl_trainer_mtime', activeId: 'p1', applying: false,
    lsGet: key => storage.get(key) ?? null,
    lsSet: (key, value) => storage.set(key, value),
    scheduleFileWrite: () => {},
  });
  vm.runInContext(section('function defaultState(){', 'function esc(') +
    section('function loadState(id){', 'let state = loadState(activeId);') +
    '\nlet state;\n' + section('function save(){', 'function activeName()') +
    section('function buildDump(){', 'function applyDump('), app);
  const snapshots = new Map();
  const legacyIds = apmo.filter(p => /^APMO-[ACGN]\d+$/.test(p.id)).map(p => p.id);
  const otherIds = bank.filter(p => p.source !== 'APMO').slice(0, 12).map(p => p.id);
  profiles.forEach(({ id }, index) => {
    const ids = [...legacyIds.filter((_, i) => i % 4 === index), ...otherIds];
    const state = JSON.parse(JSON.stringify(app.defaultState()));
    Object.assign(state, {
      solved: Object.fromEntries(ids.map(key => [key, true])),
      attempted: Object.fromEntries(ids.map(key => [key, true])),
      attempts: ids.map((key, i) => ({ t: 1700000000000 + i, sub: bank.find(p => p.id === key).subject,
        lvl: bank.find(p => p.id === key).level, ok: true, secs: 100 + i })),
      theta: Object.fromEntries(subjects.map((s, i) => [s, 2.125 + i / 4])),
      nSub: Object.fromEntries(subjects.map((s, i) => [s, 10 + i])),
      streak: 12 + index, goal: 7, filter: 'Geometry', srcFilter: 'APMO', revealed: true,
      review: { 'APMO-N22': true }, notes: { [ids[0]]: `Saved proof ${index}` },
      gyms: [{ id: `gym-${id}`, name: 'Saved set', ids }],
      mock: { ids: ids.slice(0, 6), status: { [ids[0]]: 'solved' }, done: true },
      seen: { [ids[0]]: 23 }, dueAt: { 'APMO-N22': 42 }, tick: 123,
    });
    storage.set(stateKey(id), JSON.stringify(state));
    snapshots.set(id, state);
  });
  for (const { id } of profiles) {
    app.activeId = id;
    vm.runInContext('state = loadState(activeId); save();', app);
    assert.deepEqual(JSON.parse(storage.get(stateKey(id))), snapshots.get(id));
    assert.deepEqual(JSON.parse(JSON.stringify(app.loadState(id))), snapshots.get(id));
    const dump = app.buildDump();
    assert.equal(dump._app, 'islgrind');
    assert.equal(dump._v, 1);
    assert.equal(dump[profileKey], JSON.stringify(manifest));
    for (const profile of profiles) {
      assert.deepEqual(JSON.parse(dump[stateKey(profile.id)]), snapshots.get(profile.id));
    }
  }
});
