const assert = require('node:assert/strict');
const { readFileSync } = require('node:fs');
const { join } = require('node:path');
const { test } = require('node:test');
const vm = require('node:vm');

const root = join(__dirname, '..');
const html = readFileSync(join(root, 'index.html'), 'utf8');
const subjects = ['Algebra', 'Combinatorics', 'Geometry', 'Number Theory'];

function section(start, end) {
  const from = html.indexOf(start);
  const to = html.indexOf(end, from);
  assert.ok(from >= 0 && to > from, `Cannot find application section: ${start}`);
  return html.slice(from, to);
}

// Execute the application's functions, stubbing only storage, rendering and the
// adaptive target. Selection tests fix that target so random values control the
// problem draw alone; the existing adaptive difficulty calculation stays intact.
function app(bank, saved = {}, target = 3) {
  let random = 0;
  let stored = JSON.stringify(saved);
  let saveCount = 0;
  let renderCount = 0;
  const math = Object.create(Math);
  math.random = () => random;
  const context = vm.createContext({
    BANK: bank,
    maxLevel: Math.max(1, ...bank.map(p => p.level)),
    SUBJECTS: subjects,
    Math: math,
    lsGet: () => stored,
    SKEY: id => id,
    save: () => { saveCount++; },
    renderAll: () => { renderCount++; },
    fixedTarget: target,
  });
  vm.runInContext(
    section('function defaultState(){', 'function esc(') +
    section('function loadState(id){', 'let state = loadState(activeId);') +
    '\nlet state = loadState("test");\n' +
    section('const W=1.1', 'const overallLevel') +
    section('let board=[null,null,null,null];', '/* ---------- rendering ---------- */') +
    '\nzpdTarget = () => fixedTarget;\n' +
    `globalThis.api = {
      pickProblem, queueReview, dealAll, showFilterBoard, restoreBoard, syncBoard,
      get state() { return state; },
      get board() { return board; },
      reload() { state = loadState("test"); restoreBoard(); }
    };`,
    context,
    { filename: 'index.html:problem-selection' }
  );
  return {
    ...context.api,
    get state() { return context.api.state; },
    ids: () => Array.from(context.api.board, p => p ? p.id : null),
    random: value => { random = value; },
    target: value => { context.fixedTarget = value; },
    persist: () => { stored = JSON.stringify(context.api.state); },
    get saveCount() { return saveCount; },
    get renderCount() { return renderCount; },
  };
}

function problem(id, level = 3, subject = 'Algebra', source = 'ISL') {
  return { id, level, subject, source };
}

function draw(harness, value, subject = 'Algebra', excluded = []) {
  harness.random(value);
  return harness.pickProblem(subject, new Set(excluded));
}

test('every eligible question has the same random interval despite seen/review history', () => {
  const bank = Array.from({ length: 8 }, (_, i) => problem(`A${i}`));
  const harness = app(bank, {
    seen: { A0: 500, A1: 1, A2: 99, A3: 4, A4: 23, A5: 8, A6: 12 },
    review: { A1: true, A3: true, A5: true },
    dueAt: { A1: -100, A3: 0, A5: 999999 },
    picks: { Algebra: 1000 },
    missed: { A1: 8, A3: 1 },
    tick: 1000,
  });
  // Eight equal bins have exactly representable boundaries. Probe both ends
  // and the midpoint of each bin; no frequency thresholds or flaky sampling.
  for (let i = 0; i < bank.length; i++) {
    for (const value of [i / 8, (i + 0.5) / 8, (i + 1) / 8 - Number.EPSILON]) {
      assert.equal(draw(harness, value).id, bank[i].id, `random=${value}`);
    }
  }
});

test('due review questions do not force a different difficulty level', () => {
  const harness = app([problem('due-easy', 1), problem('target', 3), problem('due-hard', 8)], {
    review: { 'due-easy': true, 'due-hard': true },
    dueAt: { 'due-easy': -1, 'due-hard': -2 },
  });
  assert.equal(draw(harness, 0).id, 'target');
  assert.equal(draw(harness, 1 - Number.EPSILON).id, 'target');
});

test('review markers do not remove otherwise eligible questions from random draws', () => {
  const bank = [problem('fresh'), problem('skipped'), problem('failed')];
  const harness = app(bank);
  harness.queueReview(bank[1]);
  harness.queueReview(bank[2]);
  assert.equal(harness.state.review.skipped, true);
  assert.equal(harness.state.review.failed, true);
  for (let i = 0; i < bank.length; i++) {
    assert.equal(draw(harness, (i + 0.5) / bank.length).id, bank[i].id);
  }
});

test('topic/source filters, solved questions and occupied cards restrict the pool', () => {
  const bank = [
    problem('other-topic', 3, 'Geometry'), problem('other-source', 3, 'Algebra', 'USAMO'),
    problem('solved'), problem('occupied'), problem('eligible-1'), problem('eligible-2'),
  ];
  const harness = app(bank, { srcFilter: 'ISL', solved: { solved: true } });
  assert.equal(draw(harness, 0, 'Algebra', ['occupied']).id, 'eligible-1');
  assert.equal(draw(harness, 1 - Number.EPSILON, 'Algebra', ['occupied']).id, 'eligible-2');
  harness.state.srcFilter = 'USAMO';
  assert.equal(draw(harness, 0).id, 'other-source');
  harness.state.srcFilter = 'all';
  assert.equal(draw(harness, 0, 'Geometry').id, 'other-topic');
});

test('unseen questions at a different level do not displace the target-level pool', () => {
  const harness = app([problem('target', 3), problem('unseen-adjacent', 4)], {
    seen: { target: 50 }, tick: 50,
  });
  assert.equal(draw(harness, 0).id, 'target');
});

test('empty target levels retain the existing nearest-level fallback, higher level first on ties', () => {
  const bank = [problem('lower', 2), problem('higher-1', 4), problem('higher-2', 4)];
  const harness = app(bank);
  assert.equal(draw(harness, 0).id, 'higher-1');
  assert.equal(draw(harness, 0.75).id, 'higher-2');
  assert.equal(draw(harness, 0, 'Algebra', ['higher-1', 'higher-2']).id, 'lower');
  harness.state.solved.lower = true;
  assert.equal(draw(harness, 0, 'Algebra', ['higher-1', 'higher-2']), null);
});

test('empty subjects, exhausted sources and fully solved pools leave the slot empty', () => {
  assert.equal(draw(app([]), 0), null);
  const harness = app([problem('A')], { solved: { A: true } });
  assert.equal(draw(harness, 0), null);
  harness.state.solved = {};
  harness.state.srcFilter = 'missing';
  assert.equal(draw(harness, 0), null);
  harness.state.srcFilter = 'all';
  assert.equal(draw(harness, 0, 'Geometry'), null);
});

test('New set excludes duplicates within one topic but permits repeats across sets', () => {
  const bank = Array.from({ length: 8 }, (_, i) => problem(`A${i}`));
  const harness = app(bank, { filter: 'Algebra' });
  harness.dealAll();
  assert.deepEqual(harness.ids(), ['A0', 'A1', 'A2', 'A3']);
  harness.dealAll();
  assert.deepEqual(harness.ids(), ['A0', 'A1', 'A2', 'A3']);
  assert.equal(harness.saveCount, 2);
  assert.equal(harness.renderCount, 2);
});

test('New set with all topics deals one eligible question per topic', () => {
  const bank = subjects.flatMap((subject, i) => [problem(`${i}-a`, 3, subject), problem(`${i}-b`, 3, subject)]);
  const harness = app(bank);
  harness.random(0.75);
  harness.dealAll();
  assert.deepEqual(harness.ids(), ['0-b', '1-b', '2-b', '3-b']);
});

test('small single-topic pools never duplicate a question to fill a set', () => {
  const harness = app([problem('A0'), problem('A1')], { filter: 'Algebra' });
  harness.dealAll();
  assert.deepEqual(harness.ids(), ['A0', 'A1', null, null]);
});

test('switching filters restores remembered boards and reload preserves valid cards', () => {
  const bank = ['ISL', 'USAMO'].flatMap(source =>
    Array.from({ length: 8 }, (_, i) => problem(`${source}-${i}`, 3, 'Algebra', source)));
  const harness = app(bank, { filter: 'Algebra', srcFilter: 'ISL' });
  harness.dealAll();
  const original = harness.ids();
  harness.state.srcFilter = 'USAMO';
  harness.showFilterBoard();
  assert.deepEqual(harness.ids(), ['USAMO-0', 'USAMO-1', 'USAMO-2', 'USAMO-3']);
  harness.state.srcFilter = 'ISL';
  harness.random(0.99);
  harness.showFilterBoard();
  assert.deepEqual(harness.ids(), original);
  harness.persist();
  harness.reload();
  assert.deepEqual(harness.ids(), original);
});

test('legacy saved review schedules and seen history are inert after reload', () => {
  const bank = [problem('due', 1), problem('A0'), problem('A1'), problem('A2'), problem('A3')];
  const harness = app(bank, {
    filter: 'Algebra', board: [null, null, null, null],
    review: { due: true, A1: true }, dueAt: { due: -100, A1: 99999 },
    picks: { Algebra: 1000 }, seen: { A0: 500, A1: 1, A2: 100 }, tick: 1000,
  });
  harness.restoreBoard();
  assert.deepEqual(harness.ids(), ['A0', 'A1', 'A2', 'A3']);
  harness.persist();
  harness.reload();
  harness.dealAll();
  assert.deepEqual(harness.ids(), ['A0', 'A1', 'A2', 'A3']);
});

test('every real-bank question in a difficulty pool is reachable with equal-width draws', () => {
  const context = vm.createContext({ window: {} });
  for (const file of ['bank.js', 'bank_extra.js', 'bank_balkan.js', 'bank_usemo.js']) {
    vm.runInContext(readFileSync(join(root, file), 'utf8'), context, { filename: file });
  }
  const bank = Array.from(context.window.ISL_BANK);
  const pool = bank.filter(p => p.subject === 'Algebra' && p.level === 3);
  assert.ok(pool.length > 10, 'Real fixture must exercise a sizeable difficulty pool');
  const seen = Object.fromEntries(pool.map((p, i) => [p.id, i + 1]));
  const harness = app(bank, { seen, tick: pool.length });
  for (let i = 0; i < pool.length; i++) {
    assert.equal(draw(harness, (i + 0.5) / pool.length).id, pool[i].id);
  }
});
