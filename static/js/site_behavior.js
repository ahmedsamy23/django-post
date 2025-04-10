// site_behavior.js
document.addEventListener("DOMContentLoaded", function () {
    // إضافة تأثير عند فتح/إغلاق الـ navbar على الأجهزة الصغيرة
    const navbarToggler = document.querySelector(".navbar-toggler");
    const navbarCollapse = document.querySelector("#navbarNav");

    if (navbarToggler && navbarCollapse) {
        navbarToggler.addEventListener("click", function () {
            navbarCollapse.classList.toggle("show");
        });

        // إغلاق الـ navbar عند الضغط على رابط
        const navLinks = document.querySelectorAll(".nav-link");
        navLinks.forEach(link => {
            link.addEventListener("click", function () {
                if (navbarCollapse.classList.contains("show")) {
                    navbarCollapse.classList.remove("show");
                }
            });
        });
    }
});