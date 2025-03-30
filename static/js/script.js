// تأكد من تحميل DOM قبل تنفيذ الكود
document.addEventListener('DOMContentLoaded', function () {
    // مثال: إضافة تنبيه عند النقر على زر مخصص
    const customButtons = document.querySelectorAll('.btn-custom');
    customButtons.forEach(button => {
        button.addEventListener('click', function () {
            console.log('Custom button clicked!');
        });
    });

    // تأثير بسيط على الكروت عند التمرير
    const cards = document.querySelectorAll('.card');
    cards.forEach(card => {
        card.addEventListener('mouseenter', function () {
            this.style.backgroundColor = '#f1f3f5';
        });
        card.addEventListener('mouseleave', function () {
            this.style.backgroundColor = 'white';
        });
    });
});