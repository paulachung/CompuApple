document.addEventListener('DOMContentLoaded', () => {
    const productList = document.getElementById('product-list'); /*contenedor donde se mostrarán las tarjetas de productos.*/
    const productFormContainer = document.getElementById('product-form-container'); /*contenedor del formulario donde se añaden o editan productos.*/
    const productForm = document.getElementById('product-form'); /*formulario de productos que incluye los campos de nombre, descripción, precio, e imagen.*/
    const addProductBtn = document.getElementById('add-product-btn'); /*Botón que abre el formulario para agregar un nuevo producto*/
    const cancelBtn = document.getElementById('cancel-btn'); /*Botón que cierra el formulario sin guardar cambios.*/

    let products = [];
    let editProductId = null; /*Variable para rastrear si se está editando un producto (almacena su ID). 
    Si es null, indica que se está creando un producto nuevo.*/

    addProductBtn.addEventListener('click', () => {
        productFormContainer.classList.remove('hidden');
        productForm.reset();
        editProductId = null;
        document.getElementById('form-title').textContent = 'Agregar Producto';
    });

    cancelBtn.addEventListener('click', () => {
        productFormContainer.classList.add('hidden');
    });

    productForm.addEventListener('submit', (e) => {
        e.preventDefault();
        const name = document.getElementById('product-name').value;
        const description = document.getElementById('product-description').value;
        const price = document.getElementById('product-price').value;
        const image = document.getElementById('product-image').value;

        /*Si editProductId es distinto de null: Se está editando un producto. 
        Se busca el producto en el array products por su ID y se actualizan sus propiedades.
        Si editProductId es null: Se está agregando un producto nuevo. 
        Se crea un objeto con los datos del producto y un ID único generado con Date.now() 
        (una marca de tiempo), y se añade al array products.*/

        if (editProductId !== null) {
            // Edit product
            const product = products.find(p => p.id === editProductId);
            product.name = name;
            product.description = description;
            product.price = price;
            product.image = image;
        } else {
            // Add product
            const newProduct = {
                id: Date.now(),
                name,
                description,
                price,
                image
            };
            products.push(newProduct);
        }

        renderProducts();
        productFormContainer.classList.add('hidden');
        /*actualiza la lista*/
    });

    function renderProducts() {
        productList.innerHTML = '';
        products.forEach(product => {
            const card = document.createElement('div');
            card.className = 'product-card';
            card.innerHTML = `
                <img src="${product.image}" alt="${product.name}">
                <h3>${product.name}</h3>
                <p>${product.description}</p>
                <p>$${product.price}</p>
                <button onclick="editProduct(${product.id})"><i class="fas fa-edit"></i></button>
                <button onclick="deleteProduct(${product.id})"><i class="fas fa-trash"></i></button>
            `;
            productList.appendChild(card);
        });
    }

    window.editProduct = function (id) {
        const product = products.find(p => p.id === id);
        if (product) {
            document.getElementById('product-name').value = product.name;
            document.getElementById('product-description').value = product.description;
            document.getElementById('product-price').value = product.price;
            document.getElementById('product-image').value = product.image;
            document.getElementById('product-id').value = product.id;
            productFormContainer.classList.remove('hidden');
            editProductId = id;
            document.getElementById('form-title').textContent = 'Editar Producto';
        }
    }

    window.deleteProduct = function (id) {
        products = products.filter(p => p.id !== id);
        renderProducts();
    }
});
