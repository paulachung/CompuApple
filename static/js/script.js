<<<<<<< HEAD
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
=======
// Modo oscuro - localStorage
let target = document.body;
let theme = localStorage.getItem("theme");

// Verifica si hay un tema guardado y aplica el tema oscuro si existe
if (theme != null) {
    target.classList.add("theme-dark");
}

// Función para cambiar el tema
function changeTheme() {
    let theme = localStorage.getItem("theme");
    if (theme != null) {
        localStorage.removeItem("theme");
    } else {
        localStorage.setItem("theme", "theme-dark");
    }
    target.classList.toggle("theme-dark");
>>>>>>> b5a86c2ba6ea76aaeb42e3b8a442beb0adc3908a
}

// Vincular con el icono del foco
document.getElementById("toggle-btn").addEventListener("click", changeTheme);

<<<<<<< HEAD
// Menú hamburguesa
const menuToggle = document.querySelector(".menu-toggle");
const navList = document.querySelector("nav ul");

menuToggle.addEventListener("click", function () {
    navList.classList.toggle("active");
});
=======
document.querySelector('.menu-toggle').addEventListener('click', function() {
    document.querySelector('nav ul').classList.toggle('active');
});

>>>>>>> b5a86c2ba6ea76aaeb42e3b8a442beb0adc3908a
