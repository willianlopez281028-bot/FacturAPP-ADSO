
document.addEventListener("DOMContentLoaded", () => {
  const sidebar = document.getElementById("appSidebar");
  const backdrop = document.querySelector(".sidebar-backdrop");
  const toggle = document.querySelector("[data-sidebar-toggle]");
  const close = () => { sidebar?.classList.remove("open"); backdrop?.classList.remove("show"); };
  toggle?.addEventListener("click", () => {
    sidebar?.classList.toggle("open");
    backdrop?.classList.toggle("show");
  });
  backdrop?.addEventListener("click", close);
  document.querySelectorAll("[data-sidebar-close]").forEach((element) => element.addEventListener("click", close));

  document.querySelectorAll(".demo-form").forEach((form) => {
    form.addEventListener("submit", (event) => {
      event.preventDefault();
      window.alert("Esta es una demostración del frontend. La persistencia se conectará cuando se implemente el backend.");
    });
  });

  document.querySelectorAll("[data-demo-action]").forEach((button) => {
    button.addEventListener("click", () => window.alert("Acción visual de demostración. Se habilitará al integrar el backend."));
  });

  const invoiceTable = document.querySelector("#invoiceItems tbody");
  document.querySelector("[data-add-invoice-row]")?.addEventListener("click", () => {
    if (!invoiceTable) return;
    const firstRow = invoiceTable.querySelector("tr");
    const clone = firstRow.cloneNode(true);
    clone.querySelectorAll("input").forEach((input) => input.value = "");
    clone.querySelector("select").selectedIndex = 0;
    invoiceTable.appendChild(clone);
  });
  invoiceTable?.addEventListener("click", (event) => {
    const removeButton = event.target.closest(".remove-row");
    if (!removeButton) return;
    const rows = invoiceTable.querySelectorAll("tr");
    if (rows.length > 1) removeButton.closest("tr").remove();
    else window.alert("La factura debe conservar al menos una línea de producto.");
  });
});
