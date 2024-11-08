// Función para mostrar el formulario de registro
function showRegisterForm() {
    document.getElementById('login-form').classList.add('hidden');
    document.getElementById('register-form').classList.remove('hidden');

    // Ocultar los mensajes de error
    hideValidationMessages();

    document.getElementById('register-form').reset();
}

// Función para mostrar el formulario de inicio de sesión
function showLoginForm() {
    document.getElementById('register-form').classList.add('hidden');
    document.getElementById('login-form').classList.remove('hidden');

    // Ocultar los mensajes de error
    hideValidationMessages();

    document.getElementById('login-form').reset();
}

// Función para ocultar todos los mensajes de validación
function hideValidationMessages() {
    // Lista de IDs de los mensajes de error
    const errorIds = [
        "name-error",
        "email-error",
        "direccion-error",
        "telefono-error",
        "password-error"
    ];

    errorIds.forEach(id => {
        const errorElement = document.getElementById(id);
        if (errorElement) {
            errorElement.textContent = "";
            errorElement.style.display = "none";
        }
    });

    // Remover clase de error de los campos de entrada
    const inputFields = [
        "register-name",
        "register-email",
        "register-direccion",
        "register-telefono",
        "register-password"
    ];

    inputFields.forEach(id => {
        const inputElement = document.getElementById(id);
        if (inputElement) {
            inputElement.classList.remove("input-error");
        }
    });
}

// Validación del campo de nombre
document.getElementById("register-name").addEventListener("blur", function() {
    const name = this.value.trim();
    const nameError = document.getElementById("name-error");

    const namePattern = /^[a-zA-ZÀ-ÿ]+( [a-zA-ZÀ-ÿ]+)*$/;

    if (name.length < 3 || name.length > 15 || !namePattern.test(name)) {
        nameError.textContent = "Ingrese un nombre válido (solo letras, entre 3 y 15 caracteres)";
        nameError.style.display = "block";
        this.classList.add("input-error");
    } else {
        nameError.textContent = "";
        nameError.style.display = "none";
        this.classList.remove("input-error");
    }
});

// Validación del campo de correo electrónico
document.getElementById("register-email").addEventListener("blur", function() {
    const emailInput = this.value.trim();
    const emailError = document.getElementById("email-error");

    const emailPattern = /^[a-zA-Z0-9_]+@(gmail|hotmail)\.com$/;

    if (emailPattern.test(emailInput)) {
        emailError.textContent = "";
        emailError.style.display = "none";
        this.classList.remove("input-error");
    } else {
        emailError.textContent = "Ingrese un correo válido (@hotmail.com o @gmail.com)";
        emailError.style.display = "block";
        this.classList.add("input-error");
    }
});

// Validación del campo de dirección
document.getElementById("register-direccion").addEventListener("blur", function() {
    const direccionInput = this.value.trim();
    const direccionError = document.getElementById("direccion-error");

    const direccionPattern = /^[a-zA-Z0-9\s,.-]+$/;

    if (direccionInput.length < 5 || !direccionPattern.test(direccionInput)) {
        direccionError.textContent = "Ingrese una dirección válida (solo letras, números, comas y puntos)";
        direccionError.style.display = "block";
        this.classList.add("input-error");
    } else {
        direccionError.textContent = "";
        direccionError.style.display = "none";
        this.classList.remove("input-error");
    }
});

// Validación del campo de número de teléfono
document.getElementById("register-telefono").addEventListener("blur", function() {
    const telefonoInput = this.value.trim();
    const telefonoError = document.getElementById("telefono-error");

    const telefonoPattern = /^[0-9]+$/;

    if (telefonoInput.length < 6 || telefonoInput.length > 15 || !telefonoPattern.test(telefonoInput)) {
        telefonoError.textContent = "Ingrese un número de teléfono válido (solo números, entre 6 y 15 dígitos)";
        telefonoError.style.display = "block";
        this.classList.add("input-error");
    } else {
        telefonoError.textContent = "";
        telefonoError.style.display = "none";
        this.classList.remove("input-error");
    }
});

// Validación del campo de contraseña
document.getElementById("register-password").addEventListener("blur", function() {
    const passwordInput = this.value.trim();
    const passwordError = document.getElementById("password-error");

    const passwordPattern = /^(?=.*[a-z])(?=.*[A-Z]{1})(?=.*\d{1})(?=.*[!@#$%^&*()_+[\]{};':"\\|,.<>?`~]{1})[^\s]{6,16}$/;

    if (!passwordPattern.test(passwordInput)) {
        passwordError.textContent = "La contraseña debe contener una mayúscula, un número, un carácter especial, al menos una minúscula, y tener entre 6 y 16 caracteres";
        passwordError.style.display = "block";
        this.classList.add("input-error");
    } else {
        passwordError.textContent = "";
        passwordError.style.display = "none";
        this.classList.remove("input-error");
    }
});

// Mostrar el mensaje de error en la página de inicio de sesión
window.onload = function() {
    const errorMessage = localStorage.getItem("registrationError");
    if (errorMessage) {
        alert(errorMessage); // Mostrar el mensaje de error
        localStorage.removeItem("registrationError"); // Limpiar el mensaje después de mostrarlo
    }
};

// Validación de cada campo del formulario
function validateField(inputElement, pattern, errorMessage) {
    const errorElement = document.getElementById(`${inputElement.id}-error`);
    const value = inputElement.value.trim();

    if (!pattern.test(value) || value === "") {
        errorElement.textContent = errorMessage;
        errorElement.style.display = "block";
        inputElement.classList.add("input-error");
        return false;
    } else {
        errorElement.textContent = "";
        errorElement.style.display = "none";
        inputElement.classList.remove("input-error");
        return true;
    }
}

// Función para validar el formulario completo
function validateForm() {
    const registerButton = document.getElementById('register-button');

    const nombre = document.getElementById('register-name');
    const email = document.getElementById('register-email');
    const direccion = document.getElementById('register-direccion');
    const telefono = document.getElementById('register-telefono');
    const password = document.getElementById('register-password');

    // Validación de cada campo
    const isNombreValid = validateField(nombre, /^[a-zA-ZÀ-ÿ]+( [a-zA-ZÀ-ÿ]+)*$/, "Ingrese un nombre válido (solo letras, entre 3 y 15 caracteres)");
    const isEmailValid = validateField(email, /^[a-zA-Z0-9_]+@(gmail|hotmail)\.com$/, "Ingrese un correo válido (@hotmail.com o @gmail.com)");
    const isDireccionValid = validateField(direccion, /^[a-zA-Z0-9\s,.-]{5,}$/, "Ingrese una dirección válida (solo letras, números, comas y puntos)");
    const isTelefonoValid = validateField(telefono, /^[0-9]{6,15}$/, "Ingrese un número de teléfono válido (solo números, entre 6 y 15 dígitos)");
    const isPasswordValid = validateField(password, /^(?=.*[a-z])(?=.*[A-Z]{1})(?=.*\d{1})(?=.*[!@#$%^&*()_+[\]{};':"\\|,.<>?`~]{1})[^\s]{6,16}$/, "La contraseña debe contener una mayúscula, un número, un carácter especial, al menos una minúscula, y tener entre 6 y 16 caracteres");

    // Deshabilitar el botón si hay algún campo inválido
    const isValid = isNombreValid && isEmailValid && isDireccionValid && isTelefonoValid && isPasswordValid;
    registerButton.disabled = !isValid;
}

// Agregar evento de input a cada campo
document.querySelectorAll('#register-form input').forEach(input => {
    input.addEventListener('input', validateForm);
});



// Botón volver arriba
var btnSubir = document.getElementById("btn-subir-arriba");
btnSubir.onclick = function () {
    window.scrollTo({ top: 0, behavior: 'smooth' });
};

let lastScrollPosition = 0;
// Mostrar el botón cuando se hace scroll
window.onscroll = function () {
    if (document.body.scrollTop > 100 || document.documentElement.scrollTop > 100) {
        btnSubir.style.display = "block";
    } else {
        btnSubir.style.display = "none";
    }
};
