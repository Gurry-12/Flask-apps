// =======================================
// COMMUNITY JS
// =======================================

document.addEventListener("DOMContentLoaded", () => {
  // Like buttons
  const likeBtns = document.querySelectorAll(".like-btn");
  likeBtns.forEach((btn) => {
    btn.addEventListener("click", () => {
      let count = parseInt(btn.dataset.likes) || 0;
      count++;
      btn.dataset.likes = count;
      btn.textContent = `👍 ${count}`;
      showToast("You liked this post!", "success");
    });
  });

  // Share buttons
  const shareBtns = document.querySelectorAll(".share-btn");
  shareBtns.forEach((btn) => {
    btn.addEventListener("click", () => {
      showToast("Share functionality coming soon!", "info");
    });
  });
});
