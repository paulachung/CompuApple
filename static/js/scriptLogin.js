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
// No es necesario manejar el inicio de sesión aquí; el formulario lo enviará automáticamente
=======
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
>>>>>>> 1fa703adf2c5159cf9ef7bfc6c7537a02351e6a2
// Función para manejar el registro
//function register() {
    //const name = document.getElementById('register-name').value;
    //const email = document.getElementById('register-email').value;
    //const password = document.getElementById('register-password').value;

    //console.log(`Registro: ${name}, ${email}`);
//}

<<<<<<< HEAD
// Botón volver arriba
=======
<<<<<<< HEAD
// boton volver arriba
=======
// Botón volver arriba
>>>>>>> origin/master
>>>>>>> 1fa703adf2c5159cf9ef7bfc6c7537a02351e6a2
var btnSubir = document.getElementById("btn-subir-arriba");
btnSubir.onclick = function () {
    window.scrollTo({ top: 0, behavior: 'smooth' });
};

let lastScrollPosition = 0;
<<<<<<< HEAD
// Mostrar el botón cuando se hace scroll
=======
<<<<<<< HEAD
// mostrar cuando hace scroll
=======
// Mostrar el botón cuando se hace scroll
>>>>>>> origin/master
>>>>>>> 1fa703adf2c5159cf9ef7bfc6c7537a02351e6a2
window.onscroll = function () {
    if (document.body.scrollTop > 100 || document.documentElement.scrollTop > 100) {
        btnSubir.style.display = "block";
    } else {
        btnSubir.style.display = "none";
    }
};
