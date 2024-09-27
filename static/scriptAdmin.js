document.addEventListener('DOMContentLoaded', () => {
    const productList = document.getElementById('product-list');
    const productFormContainer = document.getElementById('product-form-container');
    const productForm = document.getElementById('product-form');
    const addProductBtn = document.getElementById('add-product-btn');
    const cancelBtn = document.getElementById('cancel-btn');
    const deleteSelectedBtn = document.getElementById('delete-selected-btn');
    let products = [];
    let editProductId = null;

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

        if (editProductId !== null) {
            // Editar producto
            const product = products.find(p => p.id === editProductId);
            product.name = name;
            product.description = description;
            product.price = price;
            product.image = image;
        } else {
            // Agregar producto nuevo
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
    });

    deleteSelectedBtn.addEventListener('click', () => {
        const selectedProducts = document.querySelectorAll('.product-checkbox:checked');
        selectedProducts.forEach(checkbox => {
            const productId = checkbox.getAttribute('data-id');
            products = products.filter(p => p.id !== parseInt(productId));
        });
        renderProducts();
    });

    function renderProducts() {
        productList.innerHTML = '';
        products.forEach(product => {
            const card = document.createElement('div');
            card.className = 'product-card';
            card.innerHTML = `
                <input type="checkbox" class="product-checkbox" data-id="${product.id}">
                <img src="${product.image}" alt="${product.name}">
                <h3>${product.name}</h3>
                <p>${product.description}</p>
                <p>$${product.price}</p>
                <div class="card-buttons">
                    <button class="edit-btn" data-id="${product.id}"><i class="fas fa-edit"></i></button>
                    <button class="delete-btn" data-id="${product.id}"><i class="fas fa-trash"></i></button>
                </div>
`           ;
            productList.appendChild(card);
        });

        // Asignar eventos a los botones después de renderizar las tarjetas
        document.querySelectorAll('.edit-btn').forEach(button => {
            button.addEventListener('click', (e) => {
                const productId = parseInt(e.currentTarget.getAttribute('data-id'));
                editProduct(productId);
            });
        });

        document.querySelectorAll('.delete-btn').forEach(button => {
            button.addEventListener('click', (e) => {
                e.stopPropagation(); // Evita que se seleccione el checkbox
                const productId = parseInt(button.getAttribute('data-id')); // Obtiene el ID del producto
                deleteProduct(productId); // Llama a la función que elimina el producto específico
            });
        });
    }

    function deleteProduct(id) {
        products = products.filter(product => product.id !== id); // Elimina el producto específico
        renderProducts(); // Vuelve a renderizar la lista de productos
    }

    function editProduct(id) {
        const product = products.find(p => p.id === id);
        if (product) {
            document.getElementById('product-name').value = product.name;
            document.getElementById('product-description').value = product.description;
            document.getElementById('product-price').value = product.price;
            document.getElementById('product-image').value = product.image;
            editProductId = id;
            document.getElementById('form-title').textContent = 'Editar Producto';
            productFormContainer.classList.remove('hidden');
        }
    }

    function deleteSelectedProducts() {
        const selectedProducts = document.querySelectorAll('.product-checkbox:checked');
        selectedProducts.forEach(checkbox => {
            const productId = parseInt(checkbox.getAttribute('data-id'));
            products = products.filter(p => p.id !== productId);
        });
        renderProducts();
    }
});



