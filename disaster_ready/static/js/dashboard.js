// =======================================
// DASHBOARD JS
// =======================================

// Example: Readiness Score Progress
document.addEventListener("DOMContentLoaded", () => {
  const progressBars = document.querySelectorAll(".progress-bar");
  progressBars.forEach((bar) => {
    const value = bar.getAttribute("data-progress");
    bar.style.width = `${value}%`;
  });

  // Example chart using Chart.js (needs <canvas id="readinessChart">)
  if (document.getElementById("readinessChart")) {
    const ctx = document.getElementById("readinessChart").getContext("2d");
    const readinessChart = new Chart(ctx, {
      type: "doughnut",
      data: {
        labels: ["Earthquake", "Flood", "Storm", "Fire"],
        datasets: [
          {
            data: [75, 50, 60, 40], // dynamic values
            backgroundColor: [
              "var(--color-alert-medium)",
              "var(--color-powder-blue)",
              "var(--color-soft-lavender)",
              "var(--color-dusky-blue)",
            ],
          },
        ],
      },
      options: {
        responsive: true,
        plugins: { legend: { position: "bottom" } },
      },
    });
  }
});
