(() => {
  const table = document.querySelector('#research-table');
  if (!table) return;
  const rows = [...table.tBodies[0].rows];
  const search = document.querySelector('#search'), signal = document.querySelector('#signal');
  const kinds = [...document.querySelectorAll('.view-switch [data-kind]')];
  let kind = 'all';
  [...new Set(rows.map(r => r.dataset.signal))].sort().forEach(value => {
    if (value) signal.add(new Option(value.replaceAll('_', ' '), value));
  });
  function filter() {
    const query = search.value.trim().toLowerCase();
    rows.forEach(row => { row.hidden = !row.cells[0].textContent.toLowerCase().includes(query) || (signal.value && row.dataset.signal !== signal.value) || (kind !== 'all' && row.dataset.kind !== kind); });
    const visible = rows.filter(r => !r.hidden).length;
    document.querySelector('#count').textContent = `${visible} of ${rows.length} reports`;
    document.querySelector('#empty-state').hidden = visible !== 0;
  }
  kinds.forEach(button => button.addEventListener('click', () => {
    kind = button.dataset.kind;
    kinds.forEach(other => other.setAttribute('aria-pressed', String(other === button)));
    filter();
  }));
  document.querySelector('#clear-filters').addEventListener('click', () => {
    search.value = ''; signal.value = ''; kind = 'all';
    kinds.forEach(button => button.setAttribute('aria-pressed', String(button.dataset.kind === 'all')));
    filter(); search.focus();
  });
  search.addEventListener('input', filter); signal.addEventListener('change', filter); filter();
  table.querySelectorAll('[data-sort]').forEach(button => button.addEventListener('click', () => {
    const column = Number(button.dataset.sort);
    const order = button.dataset.direction ? (button.dataset.direction === 'asc' ? 'desc' : 'asc') : (button.dataset.initialDirection || 'asc');
    const direction = order === 'asc' ? 1 : -1;
    table.querySelectorAll('[data-sort]').forEach(other => {
      delete other.dataset.direction;
      other.parentElement.removeAttribute('aria-sort');
      other.querySelector('[data-sort-indicator]').textContent = '↕';
    });
    button.dataset.direction = order;
    button.parentElement.setAttribute('aria-sort', order === 'asc' ? 'ascending' : 'descending');
    button.querySelector('[data-sort-indicator]').textContent = order === 'asc' ? '↑' : '↓';
    rows.sort((a, b) => {
      if (button.dataset.sortType === 'number') {
        const left = Number.parseFloat(a.cells[column].textContent), right = Number.parseFloat(b.cells[column].textContent);
        if (!Number.isFinite(left) && !Number.isFinite(right)) return a.cells[0].textContent.localeCompare(b.cells[0].textContent);
        if (!Number.isFinite(left)) return 1;
        if (!Number.isFinite(right)) return -1;
        return direction * (left - right) || a.cells[0].textContent.localeCompare(b.cells[0].textContent);
      }
      const left = a.cells[column].dataset.sortValue || a.cells[column].textContent;
      const right = b.cells[column].dataset.sortValue || b.cells[column].textContent;
      return direction * left.localeCompare(right);
    }).forEach(row => table.tBodies[0].append(row));
  }));
})();
