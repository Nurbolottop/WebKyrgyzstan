// Карточки слов: переворот по нажатию (мышь, палец, Enter/пробел), произношение
export function mount(root) {
  let audio;
  root.querySelectorAll('.flashcard').forEach((card) => {
    const button = card.querySelector('button[aria-pressed]');
    button.addEventListener('click', () => {
      const flipped = card.classList.toggle('is-flipped');
      button.setAttribute('aria-pressed', String(flipped));
    });
    card.querySelector('[data-audio]')?.addEventListener('click', (event) => {
      audio?.pause();
      audio = new Audio(event.currentTarget.dataset.audio);
      audio.play();
    });
  });
}
