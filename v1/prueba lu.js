document.addEventListener("DOMContentLoaded", function () {
    const productType = document.getElementById("productType");
    const macFields = document.getElementById("macFields");
    const iphoneFields = document.getElementById("iphoneFields");
    const ipadFields = document.getElementById("ipadFields");
    const airpodsFields = document.getElementById("airpodsFields");
    const appleVisionProFields = document.getElementById("appleVisionPro");
    const wachFields = document.getElementById("wachFields");
    const productModal = document.getElementById('productModal');
    const addProductBtn = document.getElementById('add-product-btn');
    const closeBtn = document.querySelector('.close');
    const productForm = document.getElementById('productForm');
    const productList = document.getElementById('productList'); // Elemento donde se mostrarán los productos
    let editProductId = null;

    // Mostrar el modal cuando se hace clic en "Agregar Producto"
    addProductBtn.addEventListener('click', () => {
        productModal.style.display = 'block';
        resetForm();
        editProductId = null;
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

    // Mostrar campos específicos según el tipo de producto
    productType.addEventListener('change', function () {
        generalFields.classList.add('hidden');
        macFields.classList.add('hidden');
        iphoneFields.classList.add('hidden');
        ipadFields.classList.add('hidden');
        airpodsFields.classList.add('hidden');
        appleVisionProFields.classList.add('hidden');
        wachFields.classList.add('hidden');

        generalFields.classList.remove('hidden');

        switch (productType.value) {
            case 'mac':
                macFields.classList.remove('hidden');
                break;
            case 'iphone':
                iphoneFields.classList.remove('hidden');
                break;
            case 'ipad':
                ipadFields.classList.remove('hidden');
                break;
            case 'airpods':
                airpodsFields.classList.remove('hidden');
                break;
            case 'appleVisionPro':
                appleVisionProFields.classList.remove('hidden');
                break;
            case 'wach':
                wachFields.classList.remove('hidden');
                break;
        }
    });

    // Enviar los datos al backend usando fetch para agregar o editar productos
    productForm.addEventListener('submit', function (event) {
        event.preventDefault(); // Prevenir el comportamiento predeterminado del formulario

        const formData = new FormData(productForm); // Recoge todos los datos del formulario
        const url = editProductId ? `/edit-product/${editProductId}` : '/add-product';

        fetch(url, {
            method: 'POST',
            body: formData
        })
            .then(response => response.json())
            .then(data => {
                if (data.status === 'success') {
                    alert('Producto guardado correctamente');
                    productModal.style.display = 'none';
                    resetForm(); // Restablecer el formulario
                    fetchProducts(); // Volver a cargar la lista de productos después de guardar
                } else {
                    alert('Error al guardar el producto: ' + data.message);
                }
            })
            .catch(error => {
                console.error('Error:', error);
            });
    });

    // Obtener productos desde el backend y mostrarlos
    function fetchProducts() {
        fetch('/get-products')
            .then(response => response.json())
            .then(data => {
                renderProducts(data.products); // Pasar los productos obtenidos a la función de renderizado
            })
            .catch(error => {
                console.error('Error al obtener los productos:', error);
            });
    }

    function renderProducts(products) {
        productList.innerHTML = ''; // Limpiar la lista existente

        products.forEach(product => {
            const imageSrc = product.imagen ? product.imagen : 'static/default-image.png'; // Default image
            const card = document.createElement('div');
            card.className = 'product-card';
            card.innerHTML = `
                <input type="checkbox" class="product-checkbox" data-id="${product.id}">
                <img src="${imageSrc}" alt="${product.productName}">
                <p>${product.productName}</p>
                <p>Precio: ${product.price}</p>
                <p>Tipo: ${product.productType}</p>
                <div class="actions">
                    <button class="edit-btn" data-id="${product.id}">Editar</button>
                </div>
            `;
            productList.appendChild(card);

            // Agregar funcionalidad de edición
            const editBtn = card.querySelector('.edit-btn');
            editBtn.addEventListener('click', () => {
                editProduct(product.id);
            });
        });
    }

    function editProduct(productId) {
        fetch(`/get-product/${productId}`)
            .then(response => response.json())
            .then(data => {
                if (data.product) {
                    const product = data.product;
                    document.getElementById('productName').value = product.productName;
                    document.getElementById('price').value = product.precio;
                    productType.value = product.productType;
                    productType.dispatchEvent(new Event('change')); // Mostrar campos específicos
                    productModal.style.display = 'block';
                    editProductId = productId;
                    document.getElementById('form-title').textContent = 'Editar Producto';
                } else {
                    alert('El producto no se encontró.');
                }
            })
            .catch(error => {
                console.error('Error al obtener el producto:', error);
                alert('Hubo un error al cargar los datos del producto. Por favor, inténtalo de nuevo.');
            });
    }


    // Limpiar el formulario
    function resetForm() {
        productForm.reset();
        const fieldSections = [macFields, iphoneFields, ipadFields, airpodsFields, appleVisionProFields, wachFields];
        fieldSections.forEach(section => section.classList.add('hidden'));
        productType.value = '';
        editProductId = null;
    }


    // Obtener y mostrar productos al cargar la página
    fetchProducts();
});
