/* Close Protection & Executive Security — Main JS
   Typewriter animation, quote form, smooth scroll, list filter.
   CyberGuard handles: header state, mobile nav, scroll reveal (WOW.js), FAQ accordion (Bootstrap 5).
*/

(function () {
    'use strict';

    // ===== SCROLL HINT FADE ON SCROLL =====
    var scrollHints = document.querySelectorAll('.scroll-hint');
    if (scrollHints.length) {
        var ticking = false;
        window.addEventListener('scroll', function () {
            if (!ticking) {
                window.requestAnimationFrame(function () {
                    var scrollY = window.scrollY;
                    if (scrollY > 80) {
                        scrollHints.forEach(function (hint) { hint.style.opacity = '0'; });
                    } else {
                        scrollHints.forEach(function (hint) { hint.style.opacity = '1'; });
                    }
                    ticking = false;
                });
                ticking = true;
            }
        }, { passive: true });
    }

    // ===== QUOTE FORM SUBMISSION =====
    var forms = document.querySelectorAll('.de_form');
    forms.forEach(function (form) {
        var successMsg = form.closest('section').querySelector('.quote-success');
        if (!successMsg) return;

        form.addEventListener('submit', function (e) {
            e.preventDefault();

            var required = form.querySelectorAll('[required]');
            var valid = true;
            required.forEach(function (field) {
                if (!field.value.trim()) {
                    field.classList.add('field-error');
                    valid = false;
                } else {
                    field.classList.remove('field-error');
                }
            });

            var emailField = form.querySelector('[type="email"]');
            if (emailField && emailField.value && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(emailField.value)) {
                emailField.classList.add('field-error');
                valid = false;
            }

            var honeypot = form.querySelector('[name="website"]');
            if (honeypot && honeypot.value) return;

            if (!valid) return;

            var endpoint = form.getAttribute('action');
            if (!endpoint) {
                form.hidden = true;
                successMsg.hidden = false;
                return;
            }

            var data = new FormData(form);
            data.delete('website');

            fetch(endpoint, { method: 'POST', body: data })
                .then(function (res) {
                    if (res.ok) {
                        form.hidden = true;
                        successMsg.hidden = false;
                    }
                })
                .catch(function () { /* silent */ });
        });
    });

    // ===== SMOOTH SCROLL for anchor links =====
    document.querySelectorAll('a[href^="#"]').forEach(function (link) {
        link.addEventListener('click', function (e) {
            var target = document.querySelector(link.getAttribute('href'));
            if (target) {
                e.preventDefault();
                target.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
        });
    });

    // ===== LIST PAGE SEARCH / FILTER =====
    var filterInput = document.getElementById('listFilter');
    if (filterInput) {
        var targetGrid = document.getElementById('allItemsGrid');
        var filterCount = document.getElementById('filterCount');
        var noResults = document.getElementById('noResults');

        if (targetGrid) {
            var cards = targetGrid.querySelectorAll('.service-card, [class*="col-"]');
            var totalCards = cards.length;

            filterInput.addEventListener('input', function () {
                var query = filterInput.value.toLowerCase().trim();
                var visible = 0;

                cards.forEach(function (card) {
                    var title = (card.getAttribute('data-filter-title') || card.textContent || '').toLowerCase();
                    if (!query || title.indexOf(query) !== -1) {
                        card.classList.remove('hidden-card');
                        card.style.display = '';
                        visible++;
                    } else {
                        card.classList.add('hidden-card');
                        card.style.display = 'none';
                    }
                });

                if (filterCount) {
                    if (query) {
                        filterCount.textContent = visible + ' of ' + totalCards + ' shown';
                        filterCount.style.opacity = '1';
                    } else {
                        filterCount.textContent = '';
                        filterCount.style.opacity = '0';
                    }
                }

                if (noResults) {
                    if (visible === 0 && query) {
                        noResults.classList.add('show');
                    } else {
                        noResults.classList.remove('show');
                    }
                }
            });
        }
    }

    // ===== TYPEWRITER HERO ANIMATION =====
    // Single cursor types line 1, finishes, then moves to line 2
    // Disabled on mobile: CSS shows all text immediately
    var typewriterLines = document.querySelectorAll('.typewriter-line');
    var typewriterSub = document.querySelector('.typewriter-sub');
    var heroActionsReveal = document.querySelector('.hero-actions-reveal');
    var isMobile = window.innerWidth < 768;

    var LINE1_DURATION = 1800; // ms, matches CSS typewriter-reveal for line 1
    var LINE2_DURATION = 1400; // ms, shorter second line

    // On mobile, skip all typewriter setup — CSS handles static display
    if (isMobile) {
        typewriterLines.forEach(function (line) {
            line.style.width = '100%';
            line.style.opacity = '1';
            line.classList.add('typing-done');
        });
        if (typewriterSub) {
            typewriterSub.style.opacity = '1';
        }
        if (heroActionsReveal) {
            heroActionsReveal.style.opacity = '1';
        }
    } else {
        // Desktop: run typewriter animation
        typewriterLines.forEach(function (line) {
            line.style.width = '0';
            line.style.opacity = '0';
        });
    }

    if (!isMobile) {
        if (typewriterLines.length >= 2) {
            var line1 = typewriterLines[0];
            var line2 = typewriterLines[1];
            var line1Delay = parseInt(line1.getAttribute('data-delay') || '0', 10);
            var line2Delay = parseInt(line2.getAttribute('data-delay') || '0', 10);

            // Line 1: start typing
            setTimeout(function () {
                line1.classList.add('typing-active');
            }, line1Delay);

            // Line 1 done, transfer cursor to line 2
            setTimeout(function () {
                line1.style.width = '';
                line1.style.opacity = '';
                line1.classList.remove('typing-active');
                line1.classList.add('typing-done');
            }, line1Delay + LINE1_DURATION);

            // Line 2: start typing (use its data-delay or right after line 1)
            var line2Start = Math.max(line2Delay, line1Delay + LINE1_DURATION + 200);
            setTimeout(function () {
                line2.style.animation = 'typewriter-reveal ' + LINE2_DURATION + 'ms steps(20) forwards, typewriter-blink 0.6s step-end infinite';
                line2.classList.add('typing-active');
            }, line2Start);
        } else if (typewriterLines.length === 1) {
            var singleLine = typewriterLines[0];
            var singleDelay = parseInt(singleLine.getAttribute('data-delay') || '0', 10);
            setTimeout(function () {
                singleLine.classList.add('typing-active');
            }, singleDelay);
        }

        if (typewriterSub) {
            var subDelay = parseInt(typewriterSub.getAttribute('data-delay') || '0', 10);
            typewriterSub.style.animationPlayState = 'paused';
            setTimeout(function () {
                typewriterSub.style.animationPlayState = 'running';
            }, subDelay);
        }

        if (heroActionsReveal) {
            var actionsDelay = parseInt(heroActionsReveal.getAttribute('data-delay') || '0', 10);
            heroActionsReveal.style.animationPlayState = 'paused';
            setTimeout(function () {
                heroActionsReveal.style.animationPlayState = 'running';
            }, actionsDelay);
        }
    }

})();
