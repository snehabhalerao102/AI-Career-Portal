 /* main.js – AI Smart Career Portal */

document.addEventListener('DOMContentLoaded', () => {

  // ── Auto-dismiss flash alerts after 4 s ────────────────────────────────────
  document.querySelectorAll('.alert-dismissible').forEach(alert => {
    setTimeout(() => {
      const bsAlert = bootstrap.Alert.getOrCreateInstance(alert);
      if (bsAlert) bsAlert.close();
    }, 4000);
  });

  // ── Animate stat numbers (count-up) ────────────────────────────────────────
  document.querySelectorAll('[data-countup]').forEach(el => {
    const target = parseInt(el.dataset.countup, 10);
    let current  = 0;
    const step   = Math.ceil(target / 50);
    const timer  = setInterval(() => {
      current += step;
      if (current >= target) { current = target; clearInterval(timer); }
      el.textContent = current;
    }, 25);
  });

  // ── Skill-chart (dashboard) ─────────────────────────────────────────────────
  const skillChartEl = document.getElementById('skillChart');
  if (skillChartEl) {
    const labels = JSON.parse(skillChartEl.dataset.labels || '[]');
    const values = JSON.parse(skillChartEl.dataset.values || '[]');

    new Chart(skillChartEl, {
      type: 'doughnut',
      data: {
        labels,
        datasets: [{
          data: values,
          backgroundColor: [
            '#4f46e5','#7c3aed','#06b6d4','#10b981','#f59e0b','#ef4444','#ec4899'
          ],
          borderWidth: 0,
          hoverOffset: 8,
        }]
      },
      options: {
        responsive: true,
        cutout: '68%',
        plugins: {
          legend: {
            position: 'bottom',
            labels: { padding: 16, font: { size: 12 }, boxWidth: 12, boxHeight: 12 }
          }
        }
      }
    });
  }

  // ── Career match bar animation ──────────────────────────────────────────────
  document.querySelectorAll('.match-bar-fill').forEach(bar => {
    const pct = bar.dataset.pct || 0;
    bar.style.width = '0%';
    setTimeout(() => { bar.style.width = pct + '%'; }, 100);
    if (pct >= 70)      bar.classList.add('high');
    else if (pct >= 40) bar.classList.add('mid');
    else                bar.classList.add('low');
  });

  // ── Internship / career search – live filter hint ──────────────────────────
  const searchInput = document.getElementById('searchInput');
  if (searchInput) {
    searchInput.addEventListener('keydown', e => {
      if (e.key === 'Enter') e.target.closest('form').submit();
    });
  }

  // ── Profile skill checkbox highlight ───────────────────────────────────────
  document.querySelectorAll('.skill-checkbox').forEach(cb => {
    const label = cb.closest('label') || cb.parentElement;
    const update = () => {
      if (cb.checked) label.classList.add('skill-checked');
      else            label.classList.remove('skill-checked');
    };
    update();
    cb.addEventListener('change', update);
  });
});
