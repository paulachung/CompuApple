// Función para mostrar el formulario de registro
function showRegisterForm() {
    document.getElementById('login-form').classList.add('hidden');
    document.getElementById('register-form').classList.remove('hidden');
}

// Función para mostrar el formulario de inicio de sesión
function showLoginForm() {
    document.getElementById('register-form').classList.add('hidden');
    document.getElementById('login-form').classList.remove('hidden');
}

// Función para manejar el inicio de sesión
function login() {
    const isAdmin = document.getElementById('admin-checkbox').checked;
    const email = document.getElementById('login-email').value;
    const password = document.getElementById('login-password').value;

    console.log(`Iniciar sesión: ${email}, Admin: ${isAdmin}`);
}

// Función para manejar el registro
function register() {
    const name = document.getElementById('register-name').value;
    const email = document.getElementById('register-email').value;
    const password = document.getElementById('register-password').value;

    console.log(`Registro: ${name}, ${email}`);
}

// boton volver arriba
var btnSubir = document.getElementById("btn-subir-arriba");
btnSubir.onclick = function () {
    window.scrollTo({ top: 0, behavior: 'smooth' });
};

let lastScrollPosition = 0;
// mostrar cuando hace scroll
window.onscroll = function () {
    if (document.body.scrollTop > 100 || document.documentElement.scrollTop > 100) {
        btnSubir.style.display = "block";
    } else {
        btnSubir.style.display = "none";
    }
};
