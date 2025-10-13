// =======================================
// PROFILE JS
// =======================================

document.addEventListener("DOMContentLoaded", () => {
  const togglePassword = document.querySelector("#toggle-password");
  const passwordInput = document.querySelector("#password");

  if (togglePassword && passwordInput) {
    togglePassword.addEventListener("click", () => {
      if (passwordInput.type === "password") {
        passwordInput.type = "text";
        togglePassword.textContent = "Hide";
      } else {
        passwordInput.type = "password";
        togglePassword.textContent = "Show";
      }
    });
  }
});
