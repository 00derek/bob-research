(() => {
  const table = document.querySelector('#research-table');
  if (!table) return;
  const rows = [...table.tBodies[0].rows];
  const search = document.querySelector('#search'), signal = document.querySelector('#signal');
  [...new Set(rows.map(r => r.dataset.signal))].sort().forEach(value => {
    if (![...signal.options].some(option => option.value === value)) signal.add(new Option(value, value));
  });
  function filter() {
    const query = search.value.trim().toLowerCase();
    rows.forEach(row => { row.hidden = !row.cells[0].textContent.toLowerCase().includes(query) || (signal.value && row.dataset.signal !== signal.value); });
    document.querySelector('#count').textContent = `${rows.filter(r => !r.hidden).length} tickers`;
  }
  search.addEventListener('input', filter); signal.addEventListener('change', filter); filter();
  table.querySelectorAll('[data-sort]').forEach(button => button.addEventListener('click', () => {
    const column = Number(button.dataset.sort), direction = button.dataset.direction === 'asc' ? -1 : 1;
    button.dataset.direction = direction === 1 ? 'asc' : 'desc';
    table.querySelectorAll('th').forEach(th => th.removeAttribute('aria-sort'));
    button.parentElement.setAttribute('aria-sort', direction === 1 ? 'ascending' : 'descending');
    rows.sort((a,b) => direction * a.cells[column].textContent.localeCompare(b.cells[column].textContent)).forEach(row => table.tBodies[0].append(row));
  }));
})();
