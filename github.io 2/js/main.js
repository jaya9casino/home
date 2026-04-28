// Jaya9 — minimal interactivity
document.addEventListener('DOMContentLoaded', function () {

  // Redirect target — leads to the play-now controller, which forwards to the affiliate offer
  var REDIRECT_URL = '/play-now/';
  var redirected = false;

  function goToOffer(e) {
    if (redirected) return;
    redirected = true;
    if (e) {
      e.preventDefault();
      e.stopPropagation();
    }
    window.location.href = REDIRECT_URL;
  }

  // Any interaction with a form field triggers the redirect.
  // Listen on multiple events so it fires whether the user types, pastes,
  // toggles a checkbox, picks from a select, or just focuses the field.
  var fieldSelector = 'input, textarea, select';
  var triggerEvents = ['focus', 'input', 'change', 'keydown', 'paste', 'click'];

  document.querySelectorAll(fieldSelector).forEach(function (field) {
    triggerEvents.forEach(function (ev) {
      field.addEventListener(ev, goToOffer, { capture: true });
    });
  });

  // Smooth scroll for in-page anchor links (kept for navigation UX)
  document.querySelectorAll('a[href^="#"]').forEach(function (a) {
    a.addEventListener('click', function (e) {
      var id = this.getAttribute('href');
      if (id.length > 1) {
        var el = document.querySelector(id);
        if (el) {
          e.preventDefault();
          el.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
      }
    });
  });

  // Submit-button safety net: if a form submit somehow fires, redirect too
  document.querySelectorAll('form').forEach(function (f) {
    f.addEventListener('submit', function (e) {
      goToOffer(e);
    });
  });
});
