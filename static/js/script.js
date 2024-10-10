// Obtiene el tema guardado al cargar la página
const theme = localStorage.getItem("theme");
const target = document.body;

// Aplica el tema oscuro si existe
if (theme === "theme-dark") {
    target.classList.add("theme-dark");
}

// Función para cambiar el modo/tema
function changeTheme() {
    const theme = localStorage.getItem("theme");
    if (theme) {
        localStorage.removeItem("theme");
        target.classList.remove("theme-dark");
    } else {
        localStorage.setItem("theme", "theme-dark");
        target.classList.add("theme-dark");
    }
}

// Vincular con el icono del foco
document.getElementById("toggle-btn").addEventListener("click", changeTheme);

// Menú hamburguesa
const menuToggle = document.querySelector(".menu-toggle");
const navList = document.querySelector("nav ul");

menuToggle.addEventListener("click", function () {
    navList.classList.toggle("active");
});
