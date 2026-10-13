// Короткие подписи для игр на трёх языках (тексты контента приходят с сервера)
const STRINGS = {
  ky: { where: 'Бул кайда жайгашкан:', correct: 'Туура!', wrong: 'Туура эмес', score: 'Упай', again: 'Кайра ойноо', done: 'Азаматсың!', step: 'Кадам', choose: 'Туура бөлүктү танда', next: 'Андан ары' },
  ru: { where: 'Найди на карте:', correct: 'Верно!', wrong: 'Не совсем', score: 'Очки', again: 'Играть ещё', done: 'Молодец!', step: 'Шаг', choose: 'Выбери нужную часть', next: 'Дальше' },
  en: { where: 'Find on the map:', correct: 'Correct!', wrong: 'Not quite', score: 'Score', again: 'Play again', done: 'Well done!', step: 'Step', choose: 'Choose the right part', next: 'Next' },
};

export const t = STRINGS[document.documentElement.lang] || STRINGS.en;
