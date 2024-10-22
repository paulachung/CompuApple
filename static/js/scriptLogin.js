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

<<<<<<< HEAD
// Función para manejar el inicio de sesión
function login() {
    const isAdmin = document.getElementById('admin-checkbox').checked;
    const email = document.getElementById('login-email').value;
    const password = document.getElementById('login-password').value;

    console.log(`Iniciar sesión: ${email}, Admin: ${isAdmin}`);
}

=======
// No es necesario manejar el inicio de sesión aquí; el formulario lo enviará automáticamente
>>>>>>> origin/master
// Función para manejar el registro
function register() {
    const name = document.getElementById('register-name').value;
    const email = document.getElementById('register-email').value;
    const password = document.getElementById('register-password').value;

    console.log(`Registro: ${name}, ${email}`);
}

<<<<<<< HEAD
// boton volver arriba
=======
// Botón volver arriba
>>>>>>> origin/master
var btnSubir = document.getElementById("btn-subir-arriba");
btnSubir.onclick = function () {
    window.scrollTo({ top: 0, behavior: 'smooth' });
};

let lastScrollPosition = 0;
<<<<<<< HEAD
// mostrar cuando hace scroll
=======
// Mostrar el botón cuando se hace scroll
>>>>>>> origin/master
window.onscroll = function () {
    if (document.body.scrollTop > 100 || document.documentElement.scrollTop > 100) {
        btnSubir.style.display = "block";
    } else {
        btnSubir.style.display = "none";
    }
};
