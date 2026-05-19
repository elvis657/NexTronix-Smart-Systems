document.addEventListener('DOMContentLoaded', () => {

    // === NAVBAR SCROLL EFFECT ===
    const navbar = document.getElementById('navbar');
    let lastScroll = 0;

    window.addEventListener('scroll', () => {
        const currentScroll = window.pageYOffset;
        if (currentScroll > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
        lastScroll = currentScroll;
    });

    // === MOBILE MENU TOGGLE ===
    const navToggle = document.getElementById('navToggle');
    const navMenu = document.getElementById('navMenu');

    navToggle.addEventListener('click', () => {
        navToggle.classList.toggle('active');
        navMenu.classList.toggle('active');
    });

    document.querySelectorAll('.nav-menu a').forEach(link => {
        link.addEventListener('click', () => {
            navToggle.classList.remove('active');
            navMenu.classList.remove('active');
        });
    });

    // === NAVBAR ACTIVE LINK ON SCROLL ===
    const sections = document.querySelectorAll('section[id]');
    const navLinks = document.querySelectorAll('.nav-menu > ul > li > a');

    function updateActiveLink() {
        let current = '';
        sections.forEach(section => {
            const sectionTop = section.offsetTop - 100;
            if (window.pageYOffset >= sectionTop) {
                current = section.getAttribute('id');
            }
        });
        navLinks.forEach(link => {
            link.classList.remove('active');
            const href = link.getAttribute('href');
            if (href === `#${current}`) {
                link.classList.add('active');
            } else if (href === '#servicios' && current && current.startsWith('servicio-')) {
                link.classList.add('active');
            }
        });
    }

    window.addEventListener('scroll', updateActiveLink);

    // === ANIMATED COUNTERS ===
    const counters = document.querySelectorAll('.stat-num');
    let countersAnimated = false;

    function animateCounters() {
        if (countersAnimated) return;
        const triggerPoint = counters[0]?.getBoundingClientRect().top;
        if (triggerPoint && triggerPoint < window.innerHeight - 100) {
            countersAnimated = true;
            counters.forEach(counter => {
                const target = parseInt(counter.getAttribute('data-target'));
                let current = 0;
                const increment = target / 60;
                const updateCounter = () => {
                    current += increment;
                    if (current < target) {
                        counter.textContent = Math.floor(current);
                        requestAnimationFrame(updateCounter);
                    } else {
                        counter.textContent = target;
                    }
                };
                updateCounter();
            });
        }
    }

    window.addEventListener('scroll', animateCounters);

    // === SCROLL REVEAL ANIMATION ===
    const revealElements = document.querySelectorAll(
        '.servicio-card, .pilar-card, .nosotros-grid, .contacto-grid, .detalle-grid'
    );

    const revealObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
                revealObserver.unobserve(entry.target);
            }
        });
    }, { threshold: 0.1 });

    revealElements.forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(30px)';
        el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        revealObserver.observe(el);
    });

    // === FORM HANDLING ===
    const form = document.getElementById('contactForm');

    form.addEventListener('submit', (e) => {
        e.preventDefault();

        const btn = form.querySelector('button[type="submit"]');
        const originalText = btn.innerHTML;
        btn.innerHTML = 'Enviando... <i class="fas fa-spinner fa-spin"></i>';
        btn.disabled = true;

        setTimeout(() => {
            btn.innerHTML = originalText;
            btn.disabled = false;
            form.reset();

            showToast('¡Cotización enviada con éxito! Te contactaremos pronto.');
        }, 1500);
    });

    // === TOAST SYSTEM ===
    function showToast(message) {
        const existing = document.querySelector('.toast');
        if (existing) existing.remove();

        const toast = document.createElement('div');
        toast.className = 'toast';
        toast.textContent = message;
        document.body.appendChild(toast);

        requestAnimationFrame(() => {
            toast.classList.add('show');
        });

        setTimeout(() => {
            toast.classList.remove('show');
            setTimeout(() => toast.remove(), 400);
        }, 4000);
    }

    // === SMOOTH SCROLL FOR ANCHOR LINKS ===
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            const targetId = this.getAttribute('href');
            if (targetId === '#') return;
            const target = document.querySelector(targetId);
            if (target) {
                e.preventDefault();
                target.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
        });
    });

    // INIT COUNTER CHECK
    setTimeout(animateCounters, 500);
});
