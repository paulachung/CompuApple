document.addEventListener("DOMContentLoaded", function () {
    const productType = document.getElementById("productType");
    const macFields = document.getElementById("macFields");
    const iphoneFields = document.getElementById("iphoneFields");
    const ipadFields = document.getElementById("ipadFields");
    const airpodsFields = document.getElementById("airpodsFields");
    const appleVisionProFields = document.getElementById("appleVisionPro");
    const wachFields = document.getElementById("wachFields");
    const generalFields = document.getElementById("generalFields");
    const productModal = document.getElementById('productModal');
    const addProductBtn = document.getElementById('add-product-btn');
    const closeBtn = document.querySelector('.close');
    const productForm = document.getElementById('productForm');
    const productList = document.getElementById('productList');
    const deleteSelectedBtn = document.getElementById('delete-selected-btn'); // Botón para eliminar seleccionados
    let editProductId = null;

    // Mostrar el modal al hacer clic en "Agregar Producto"
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

        switch (productType.value) {
            case 'mac':
                generalFields.classList.remove('hidden');
                macFields.classList.remove('hidden');
                break;
            case 'iphone':
                generalFields.classList.remove('hidden');
                iphoneFields.classList.remove('hidden');
                break;
            case 'ipad':
                generalFields.classList.remove('hidden');
                ipadFields.classList.remove('hidden');
                break;
            case 'airpods':
                generalFields.classList.remove('hidden');
                airpodsFields.classList.remove('hidden');
                break;
            case 'appleVisionPro':
                generalFields.classList.remove('hidden');
                appleVisionProFields.classList.remove('hidden');
                break;
            case 'wach':
                generalFields.classList.remove('hidden');
                wachFields.classList.remove('hidden');
                break;
            default:
                break;
        }
    });

    // Enviar los datos al backend para agregar o editar productos
    productForm.addEventListener('submit', function (event) {
        event.preventDefault();

        const formData = new FormData(productForm);
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
                    resetForm();
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
        const productList = document.getElementById('product-list');
        productList.innerHTML = ''; // Limpia la lista antes de agregar productos

        products.forEach(product => {
            // Crear una tarjeta para cada producto
            const productCard = document.createElement('div');
            productCard.className = 'product-card';

            // Agregar imagen
            const img = document.createElement('img');
            img.src = product.image_url;
            productCard.appendChild(img);

            // Agregar nombre
            const name = document.createElement('h3');
            name.textContent = product.name;
            productCard.appendChild(name);

            // Agregar descripción
            const description = document.createElement('p');
            description.textContent = product.description;
            productCard.appendChild(description);

            // Agregar precio
            const price = document.createElement('p');
            price.textContent = `$${product.price}`;
            productCard.appendChild(price);

            // Agregar tarjeta a la lista
            productList.appendChild(productCard);
        });
    }

    // Ejemplo de solicitud para obtener los productos
    fetch('/get-products')
        .then(response => response.json())
        .then(data => {
            renderProducts(data);
        })
        .catch(error => console.error('Error al obtener los productos:', error));


    function editProduct(productId) {
        fetch('/get-products')
            .then(response => response.json())
            .then(data => {
                const productToEdit = data.products.find(product => product.id === productId);
                if (productToEdit) {
                    // Rellenar el formulario con los datos del producto
                    productForm.elements['productName'].value = productToEdit.productName;
                    productForm.elements['price'].value = productToEdit.price;
                    productForm.elements['productType'].value = productToEdit.productType;
                    // Agregar otros campos específicos del producto aquí
                    editProductId = productId;
                    productModal.style.display = 'block';
                    document.getElementById('form-title').textContent = 'Editar Producto';
                }
            })
            .catch(error => console.error('Error al obtener el producto:', error));
    }

    // Función para eliminar un producto
    function deleteProduct(productId) {
        fetch(`/delete-product/${productId}`, {
            method: 'DELETE',
        })
            .then(response => response.json())
            .then(data => {
                if (data.status === 'success') {
                    alert('Producto eliminado correctamente');
                    fetchProducts(); // Recargar productos
                } else {
                    alert('Error al eliminar el producto: ' + data.message);
                }
            })
            .catch(error => {
                console.error('Error al eliminar el producto:', error);
            });
    }

    // Limpiar el formulario
    function resetForm() {
        productForm.reset();
        const fieldSections = [macFields, iphoneFields, ipadFields, airpodsFields, appleVisionProFields, wachFields, generalFields];
        fieldSections.forEach(section => section.classList.add('hidden'));
        productType.value = '';
        editProductId = null;
    }

    // Obtener y mostrar productos al cargar la página
    fetchProducts();

    // Eliminar productos seleccionados
    deleteSelectedBtn.addEventListener('click', () => {
        const selectedCheckboxes = document.querySelectorAll('.product-checkbox:checked');
        const productIds = Array.from(selectedCheckboxes).map(checkbox => checkbox.dataset.id);

        if (productIds.length === 0) {
            alert('Por favor, selecciona al menos un producto para eliminar.');
            return;
        }

        if (confirm('¿Estás seguro de que deseas eliminar los productos seleccionados?')) {
            Promise.all(productIds.map(id => fetch(`/delete-product/${id}`, { method: 'DELETE' })))
                .then(responses => Promise.all(responses.map(res => res.json())))
                .then(results => {
                    const successCount = results.filter(res => res.status === 'success').length;
                    alert(`${successCount} productos eliminados correctamente.`);
                    fetchProducts(); // Recargar productos
                })
                .catch(error => {
                    console.error('Error al eliminar productos seleccionados:', error);
                });
        }
    });

    function mostrarProductosEnTarjetas(productos) {
        const listaProductos = document.getElementById('product-list');
        listaProductos.innerHTML = ''; // Limpiar la lista antes de agregar los productos

        productos.forEach(producto => {
            const tarjeta = document.createElement('div');
            tarjeta.classList.add('product-card');

            tarjeta.innerHTML = `
                <img src="${producto.imagen}" alt="${producto.nombre}" />
                <h3>${producto.nombre}</h3>
                <p>Precio: $${producto.precio}</p>
                <div class="card-buttons">
                    <button class="editar-btn">Editar</button>
                    <button class="eliminar-btn">Eliminar</button>
                </div>
                <input type="checkbox" class="producto-checkbox">
            `;

            listaProductos.appendChild(tarjeta);
        });
    }
});

