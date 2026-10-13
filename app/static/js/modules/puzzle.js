// Загадка или ребус: ввод ответа или выбор варианта, проверка без учёта регистра и «ё»
import { normalize } from '../core/dom.js';

export function mount(root) {
  const answers = root.dataset.answers.split('|').map(normalize).filter(Boolean);
  const feedback = root.querySelector('.feedback');

  function check(value) {
    const ok = answers.includes(normalize(value));
    feedback.className = `feedback is-visible ${ok ? 'is-correct' : 'is-wrong'}`;
    feedback.innerHTML = '';
    const strong = document.createElement('strong');
    strong.textContent = ok ? feedback.dataset.correct : feedback.dataset.wrong;
    feedback.append(strong);
    return ok;
  }

  root.querySelector('form')?.addEventListener('submit', (event) => {
    event.preventDefault();
    const input = event.currentTarget.querySelector('input');
    if (check(input.value)) input.disabled = true;
  });

  root.querySelectorAll('[data-option]').forEach((button) => {
    button.addEventListener('click', () => {
      const ok = check(button.dataset.option);
      button.classList.add(ok ? 'chip--accent' : 'is-wrong');
      if (ok) root.querySelectorAll('[data-option]').forEach((b) => { b.disabled = true; });
    });
  });
}
