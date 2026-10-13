// Пошаговая инструкция: по умолчанию все шаги списком; режим «по одному шагу» включается кнопкой
export function mount(root) {
  const steps = [...root.querySelectorAll('.step')];
  if (steps.length < 2) return;
  const lang = document.documentElement.lang;
  const labels = {
    ky: ['Кадам менен', 'Бардык кадамдар'],
    ru: ['По шагам', 'Все шаги'],
    en: ['Step by step', 'All steps'],
  }[lang] || ['Step by step', 'All steps'];

  const toggle = document.createElement('button');
  toggle.type = 'button';
  toggle.className = 'btn btn--outline btn--small';
  const toolbar = document.createElement('div');
  toolbar.className = 'stepper__toolbar';
  toolbar.append(toggle);
  root.prepend(toolbar);

  const prev = root.querySelector('[data-prev]');
  const next = root.querySelector('[data-next]');
  const bar = root.querySelector('.stepper__progress span');
  const counter = root.querySelector('[data-counter]');
  let current = 0;

  function render() {
    const single = root.dataset.mode === 'single';
    toggle.textContent = single ? labels[1] : labels[0];
    steps.forEach((step, i) => step.classList.toggle('is-current', i === current));
    prev.disabled = current === 0;
    next.disabled = current === steps.length - 1;
    bar.style.width = `${((current + 1) / steps.length) * 100}%`;
    counter.textContent = `${current + 1} / ${steps.length}`;
  }

  const go = (delta) => {
    current = Math.min(steps.length - 1, Math.max(0, current + delta));
    render();
    steps[current].scrollIntoView({ block: 'nearest', behavior: 'smooth' });
  };

  toggle.addEventListener('click', () => {
    root.dataset.mode = root.dataset.mode === 'single' ? 'all' : 'single';
    render();
  });
  prev.addEventListener('click', () => go(-1));
  next.addEventListener('click', () => go(1));
  root.addEventListener('keydown', (event) => {
    if (root.dataset.mode !== 'single') return;
    if (event.key === 'ArrowRight') go(1);
    if (event.key === 'ArrowLeft') go(-1);
  });
  root.dataset.mode = 'all';
  render();
}
