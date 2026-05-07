/* RecipeShare – Main JavaScript */

document.addEventListener('DOMContentLoaded', function () {

  // ── Auto-dismiss alerts after 4 seconds ──────────────────────
  const alerts = document.querySelectorAll('.alert');
  alerts.forEach(function (alert) {
    setTimeout(function () {
      const bsAlert = new bootstrap.Alert(alert);
      bsAlert.close();
    }, 4000);
  });

  // ── Image preview on recipe form ─────────────────────────────
  const imageInput = document.getElementById('id_image');
  if (imageInput) {
    imageInput.addEventListener('change', function () {
      const preview = document.getElementById('image-preview');
      const file = this.files[0];
      if (file && preview) {
        const reader = new FileReader();
        reader.onload = function (e) {
          preview.src = e.target.result;
          preview.parentElement.style.display = 'block';
        };
        reader.readAsDataURL(file);
      }
    });
  }

  // ── Navbar active link highlight ────────────────────────────
  const currentPath = window.location.pathname;
  document.querySelectorAll('.nav-link').forEach(function (link) {
    if (link.getAttribute('href') === currentPath) {
      link.classList.add('active');
    }
  });

  // ── Smooth scroll for anchor links ──────────────────────────
  document.querySelectorAll('a[href^="#"]').forEach(function (anchor) {
    anchor.addEventListener('click', function (e) {
      const target = document.querySelector(this.getAttribute('href'));
      if (target) {
        e.preventDefault();
        target.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    });
  });

  // ── Delete confirmation modal focus ─────────────────────────
  const deleteForm = document.getElementById('delete-form');
  if (deleteForm) {
    deleteForm.addEventListener('submit', function () {
      const btn = this.querySelector('button[type="submit"]');
      if (btn) {
        btn.disabled = true;
        btn.innerHTML = '<span class="spinner-border spinner-border-sm me-1"></span> Deleting...';
      }
    });
  }

  // ── Character counter for description textarea ───────────────
  const descTextarea = document.getElementById('id_description');
  if (descTextarea) {
    const maxLen = 500;
    const counter = document.createElement('div');
    counter.className = 'form-text text-end';
    counter.style.fontSize = '0.78rem';
    descTextarea.parentElement.appendChild(counter);

    function updateCounter() {
      const remaining = maxLen - descTextarea.value.length;
      counter.textContent = `${descTextarea.value.length} / ${maxLen} characters`;
      counter.style.color = remaining < 50 ? '#dc3545' : 'var(--text-muted)';
    }

    descTextarea.addEventListener('input', updateCounter);
    updateCounter();
  }

  // ── Tooltip init (Bootstrap) ─────────────────────────────────
  const tooltipEls = document.querySelectorAll('[data-bs-toggle="tooltip"]');
  tooltipEls.forEach(function (el) {
    new bootstrap.Tooltip(el);
  });
});
