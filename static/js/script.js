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
}

// Vincular con el icono del foco
document.getElementById("toggle-btn").addEventListener("click", changeTheme);

document.querySelector('.menu-toggle').addEventListener('click', function() {
    document.querySelector('nav ul').classList.toggle('active');
});

