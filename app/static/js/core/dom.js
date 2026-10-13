export function readJSON(id) {
  const node = typeof id === 'string' ? document.getElementById(id) : id;
  return node ? JSON.parse(node.textContent) : null;
}

export function h(tag, attrs = {}, ...children) {
  const el = document.createElement(tag);
  for (const [key, value] of Object.entries(attrs)) {
    if (value === false || value == null) continue;
    if (key === 'class') el.className = value;
    else if (key === 'text') el.textContent = value;
    else if (key.startsWith('on')) el.addEventListener(key.slice(2), value);
    else el.setAttribute(key, value === true ? '' : value);
  }
  for (const child of children.flat()) {
    if (child == null || child === false) continue;
    el.append(child instanceof Node ? child : document.createTextNode(child));
  }
  return el;
}

// Сравнение ответов: регистр, ё/е, лишние пробелы и знаки не важны
export function normalize(text) {
  return (text || '')
    .toLocaleLowerCase()
    .replace(/ё/g, 'е')
    .replace(/[«»"'.,!?()-]/g, ' ')
    .replace(/\s+/g, ' ')
    .trim();
}

export function shuffle(list) {
  const copy = [...list];
  for (let i = copy.length - 1; i > 0; i -= 1) {
    const j = Math.floor(Math.random() * (i + 1));
    [copy[i], copy[j]] = [copy[j], copy[i]];
  }
  return copy;
}
