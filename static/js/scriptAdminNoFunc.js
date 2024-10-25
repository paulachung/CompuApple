document.addEventListener('DOMContentLoaded', () => {
    const productModal = document.getElementById('productModal');
    const addProductBtn = document.getElementById('add-product-btn');
    const closeBtn = document.querySelector('.close');
    const productForm = document.getElementById('product-form');
    const productList = document.getElementById('product-list');
    const deleteSelectedBtn = document.getElementById('delete-selected-btn'); // Asegúrate de que este ID es correcto
    let products = [];
    let editProductId = null;

    // Mostrar el modal cuando se hace clic en "Agregar Producto"
    addProductBtn.addEventListener('click', () => {
        productModal.style.display = 'block';
        productForm.reset();
        editProductId = null; // Limpiar el formulario
        document.getElementById('form-title').textContent = 'Agregar Producto';
    });

    // Cerrar el modal al hacer clic en la "X"
    closeBtn.addEventListener('click', () => {
        productModal.style.display = 'none';
    });

    // Cerrar el modal al hacer clic fuera de la ventana del modal
    window.addEventListener('click', (event) => {
        if (event.target === productModal) {
            productModal.style.display = 'none';
        }
    });

    // Manejo del envío del formulario
    productForm.addEventListener('submit', (e) => {
        e.preventDefault();
        const name = document.getElementById('product-name').value;
        const description = document.getElementById('product-description').value;
        const price = document.getElementById('product-price').value;
        const imageFile = document.getElementById('product-image').files[0];

        let imageUrl = '';
        if (imageFile) {
            const reader = new FileReader();
            reader.onload = function (event) {
                imageUrl = event.target.result; // Obtener la URL de la imagen
                saveProduct(name, description, price, imageUrl); // Llamar a la función para guardar
            };
            reader.readAsDataURL(imageFile); // Leer la imagen como Data URL
        } else {
            saveProduct(name, description, price, imageUrl); // Manejar caso de no imagen
        }
    });

    function saveProduct(name, description, price, imageUrl) {
        if (editProductId !== null) {
            // Editar producto existente
            const product = products.find(p => p.id === editProductId);
            product.name = name;
            product.description = description;
            product.price = price;
            product.image = imageUrl;
        } else {
            // Agregar nuevo producto
            const newProduct = {
                id: Date.now(),
                name,
                description,
                price,
                image: imageUrl
            };
            products.push(newProduct);
        }

        renderProducts();
        productModal.style.display = 'none'; // Ocultar el modal
    }

    function renderProducts() {
        productList.innerHTML = '';
        products.forEach(product => {
            const card = document.createElement('div');
            card.className = 'product-card';
            card.innerHTML = `
                <input type="checkbox" class="product-checkbox" data-id="${product.id}">
                <img src="${product.image || 'ruta/a/imagen/por/defecto.jpg'}" alt="${product.name}"> <!-- Imagen por defecto -->
                <h3>${product.name}</h3>
                <p>${product.description}</p>
                <p>$${product.price}</p>
                <div class="card-buttons">
                    <button class="edit-btn" data-id="${product.id}">Editar</button>
                    <button class="delete-btn" data-id="${product.id}">Eliminar</button>
                </div>
            `;
            productList.appendChild(card);
        });

        // Asignar eventos a los botones de editar y eliminar
        assignButtonEvents();
    }

    function assignButtonEvents() {
        document.querySelectorAll('.edit-btn').forEach(button => {
            button.addEventListener('click', (e) => {
                const productId = parseInt(e.target.getAttribute('data-id'));
                editProduct(productId);
            });
        });

        document.querySelectorAll('.delete-btn').forEach(button => {
            button.addEventListener('click', (e) => {
                const productId = parseInt(e.target.getAttribute('data-id'));
                deleteProduct(productId);
            });
        });
    }

    // Manejar la eliminación de productos seleccionados
    deleteSelectedBtn.addEventListener('click', () => {
        const checkboxes = document.querySelectorAll('.product-checkbox:checked');
        if (checkboxes.length === 0) {
            alert("Por favor, selecciona al menos un producto para eliminar.");
            return; // Salir si no hay productos seleccionados
        }

        checkboxes.forEach(checkbox => {
            const productId = parseInt(checkbox.getAttribute('data-id'));
            deleteProduct(productId);
        });
    });

    function editProduct(id) {
        const product = products.find(p => p.id === id);
        if (product) {
            document.getElementById('product-name').value = product.name;
            document.getElementById('product-description').value = product.description;
            document.getElementById('product-price').value = product.price;
            document.getElementById('product-image').value = ''; // Limpiar el campo de imagen
            editProductId = id;
            document.getElementById('form-title').textContent = 'Editar Producto';
            productModal.style.display = 'block';
        }
    }

    function deleteProduct(id) {
        if (confirm("¿Estás seguro de que deseas eliminar este producto?")) {
            products = products.filter(product => product.id !== id);
            renderProducts();
        }
    }
});

// Seleccionar el botón
var btnSubir = document.getElementById("btn-subir-arriba");

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
