function showRegisterForm() {
    document.getElementById('login-form').classList.add('hidden');
    document.getElementById('register-form').classList.remove('hidden');
}

/* Estas dos funciones controlan la visualización de los formularios de iniciar sesión y registro, 
 alternando su visibilidad mediante la manipulación de las clases hidden.*/

function showLoginForm() {
    document.getElementById('register-form').classList.add('hidden');
    document.getElementById('login-form').classList.remove('hidden');
}


function login() {
    const isAdmin = document.getElementById('admin-checkbox').checked;
    const email = document.getElementById('login-email').value;
    const password = document.getElementById('login-password').value;


    console.log(`Iniciar sesión: ${email}, Admin: ${isAdmin}`);
}

function register() {
    const name = document.getElementById('register-name').value;
    const email = document.getElementById('register-email').value;
    const password = document.getElementById('register-password').value;


    console.log(`Registro: ${name}, ${email}`);
}

