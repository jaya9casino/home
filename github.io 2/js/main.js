// Jaya9 — minimal interactivity
document.addEventListener('DOMContentLoaded', function () {
  function goToOffer(form, e) {
    if (e) {
      e.preventDefault();
      e.stopPropagation();
    }
    var target = (form && form.getAttribute('action')) || 'play-now/';
    window.location.assign(target);
  }

  document.querySelectorAll('form').forEach(function (form) {
    form.addEventListener('keydown', function (e) {
      if (e.key === 'Enter') {
        goToOffer(form, e);
      }
    });
    form.addEventListener('submit', function (e) {
      goToOffer(form, e);
    });
  });

  document.querySelectorAll('a[href^="#"]').forEach(function (a) {
    a.addEventListener('click', function (e) {
      var id = this.getAttribute('href');
      if (id && id.length > 1) {
        var el = document.querySelector(id);
        if (el) {
          e.preventDefault();
          el.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
      }
    });
  });
});
