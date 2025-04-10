// accounts_behavior.js
document.addEventListener("DOMContentLoaded", function () {
    // تأكيد الحذف في صفحة profile_delete.html
    const deleteForm = document.querySelector("form");
    if (deleteForm) {
        deleteForm.addEventListener("submit", function (e) {
            if (!confirm("Are you sure you want to delete your profile?")) {
                e.preventDefault();
            }
        });
    }

    // إضافة تأثير عند الضغط على الأزرار
    const buttons = document.querySelectorAll(".boxed-btn3");
    buttons.forEach(button => {
        button.addEventListener("click", function () {
            button.style.opacity = "0.8";
            setTimeout(() => (button.style.opacity = "1"), 200);
        });
    });
});