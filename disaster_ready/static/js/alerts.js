// =======================================
// ALERTS JS
// =======================================

document.addEventListener("DOMContentLoaded", () => {
  const alertCards = document.querySelectorAll(".alert-card");

  alertCards.forEach((card) => {
    const markReadBtn = card.querySelector(".mark-read");
    if (markReadBtn) {
      markReadBtn.addEventListener("click", () => {
        card.classList.add("read");
        showToast("Alert marked as read", "info");
        // Optional: send AJAX to backend to update DB
      });
    }
  });

  // Filter alerts
  const filterSelect = document.querySelector("#filter-alerts");
  if (filterSelect) {
    filterSelect.addEventListener("change", () => {
      const level = filterSelect.value;
      alertCards.forEach((card) => {
        if (level === "all" || card.dataset.level === level) {
          card.style.display = "flex";
        } else {
          card.style.display = "none";
        }
      });
    });
  }
});
