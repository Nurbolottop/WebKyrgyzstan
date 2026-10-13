/*
 * Точка входа. Общее поведение страниц + загрузка модулей по data-module.
 * Модуль экспортирует mount(root) и подгружается, только если он есть на странице.
 */
import { initHeader, initMenu } from './core/menu.js';
import { initReveal } from './core/reveal.js';

initHeader();
initMenu();
initReveal();

const registry = JSON.parse(document.getElementById('js-modules')?.textContent || '{}');

document.querySelectorAll('[data-module]').forEach(async (root) => {
  const src = registry[root.dataset.module];
  if (!src) return;
  try {
    const module = await import(src);
    module.mount(root);
  } catch (error) {
    console.error(`[webkg] модуль ${root.dataset.module}:`, error);
  }
});
