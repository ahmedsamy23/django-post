// Smooth Scroll for Navbar Links
document.addEventListener('DOMContentLoaded', function () {
    const navLinks = document.querySelectorAll('.nav-link');
    navLinks.forEach(link => {
        link.addEventListener('click', function (e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                window.scrollTo({
                    top: targetElement.offsetTop,
                    behavior: 'smooth'
                });
            } else {
                window.location.href = targetId; // إذا كان الرابط خارجي
            }
        });
    });

    // Fade-in effect for Hero Section
    const heroSection = document.querySelector('.hero-section');
    heroSection.style.opacity = 0;
    setTimeout(() => {
        heroSection.style.transition = 'opacity 1s ease-in-out';
        heroSection.style.opacity = 1;
    }, 500);
});