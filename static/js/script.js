// Smooth scrolling for navigation links
document.querySelectorAll('.nav-link, .btn-link').forEach(link => {
    link.addEventListener('click', function (e) {
        const href = this.getAttribute('href');
        if (href.startsWith('#')) {
            e.preventDefault();
            document.querySelector(href).scrollIntoView({ behavior: 'smooth' });
        }
    });
});

// Fade-in animation for cards on page load
document.addEventListener('DOMContentLoaded', () => {
    const cards = document.querySelectorAll('.card');
    cards.forEach((card, index) => {
        setTimeout(() => {
            card.style.opacity = '0';
            card.style.transition = 'opacity 0.5s ease';
            setTimeout(() => {
                card.style.opacity = '1';
            }, 100 * index); // تأخير متتالي لكل بطاقة
        }, 100);
    });
});