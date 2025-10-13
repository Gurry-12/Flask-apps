// =======================================
// KIT CUSTOMIZER JS
// =======================================

document.addEventListener("DOMContentLoaded", () => {
  const addItemBtn = document.querySelector("#add-kit-item");
  const kitList = document.querySelector("#kit-list");

  if (addItemBtn && kitList) {
    addItemBtn.addEventListener("click", () => {
      const itemInput = document.querySelector("#kit-item-input");
      if (!itemInput.value.trim()) return;

      const li = document.createElement("li");
      li.className = "kit-item";
      li.textContent = itemInput.value;

      const removeBtn = document.createElement("button");
      removeBtn.textContent = "Remove";
      removeBtn.className = "remove-btn";
      removeBtn.addEventListener("click", () => li.remove());

      li.appendChild(removeBtn);
      kitList.appendChild(li);

      itemInput.value = "";
      showToast("Item added to kit!", "success");
    });
  }
});
