document.addEventListener("DOMContentLoaded", function () {
    const productType = document.getElementById("productType");
    const generalFields = document.getElementById("generalFields");
    const macFields = document.getElementById("macFields");
    const iphoneFields = document.getElementById("iphoneFields");
    const ipadFields = document.getElementById("ipadFields");
    const airpodsFields = document.getElementById("airpodsFields");
    const applevisionproFields = document.getElementById("applevisionpro");
    const watchFields = document.getElementById("watchFields");
    const accesoriosFields = document.getElementById("accesorios");
    const productModal = document.getElementById('productModal');
    const addProductBtn = document.getElementById('add-product-btn');
    const closeBtn = document.querySelector('.close');
    const productForm = document.getElementById('productForm');
    const productList = document.getElementById('productList'); // Elemento donde se mostrarán los productos
    const deleteSelectedBtn = document.getElementById('delete-selected-btn'); // Botón para eliminar seleccionados

    let products = []; // Array para almacenar los productos
    let editProductId = null; // Variable para rastrear el producto que se está editando

    // Mostrar el modal cuando se hace clic en "Agregar Producto"
    addProductBtn.addEventListener('click', () => {
        productModal.style.display = 'block';
        productForm.reset();
        editProductId = null; // Limpiar el formulario
        document.getElementById('form-title').textContent = 'Agregar Producto';
    })

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

    // Agrega un evento 'change' al select para detectar cambios
    productType.addEventListener('change', function () {
        // Primero oculta todos los campos
        generalFields.classList.add('hidden');
        macFields.classList.add('hidden');
        iphoneFields.classList.add('hidden');
        ipadFields.classList.add('hidden');
        airpodsFields.classList.add('hidden');
        applevisionproFields.classList.add('hidden');
        watchFields.classList.add('hidden');
        // Muestra los campos generales
        generalFields.classList.remove('hidden');

        // Muestra los campos específicos según el tipo de producto seleccionado
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
            case 'applevisionpro':
                applevisionproFields.classList.remove('hidden');
                break;
            case 'watch':
                watchFields.classList.remove('hidden');
                break;
            case 'accesorios':
                accesoriosFields.classList.remove('hidden');
                break;
        }
    });


    // Función para manejar la adición y edición de productos
    productForm.addEventListener('submit', function (event) {
        event.preventDefault(); // Evita el envío del formulario
        const productName = document.getElementById('productName').value;
        const price = document.getElementById('price').value;
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

        let productDetails = {
            id: editProductId ? editProductId : Date.now(), // Usa el ID si está editando, o genera uno nuevo
            name: productName,
            price: price,
            type: productType.value
        };

        // Agrega detalles específicos según el tipo de producto
        switch (productType.value) {
            case 'mac':
                productDetails.screenSizeMac = document.getElementById('screenSizeMac').value;
                productDetails.capacidadMac = document.getElementById('capacidadMac').value;
                productDetails.memoriaMac = document.getElementById('memoriaMac').value;
                productDetails.procesadorMac = document.getElementById('procesadorMac').value;
                productDetails.softwareMac = document.getElementById('softwareMac').value;
                productDetails.conexionInalambricaMac = document.getElementById('conexionInalambricaMac').value;
                productDetails.audioMac = document.getElementById('audioMac').value;
                productDetails.tecladoMac = document.getElementById('tecladoMac').value;
                productDetails.camaraMac = document.getElementById('camaraMac').value;
                productDetails.formatoMac = document.getElementById('formatoMac').value;
                productDetails.bateriaMac = document.getElementById('bateriaMac').value;
                break;

            case 'iphone':
                productDetails.screenSizeIphone = document.getElementById('screenSizeIphone').value;
                productDetails.resolutionIphone = document.getElementById('resolutionIphone').value;
                productDetails.resistenciaIphone = document.getElementById('resistenciaIphone').value;
                productDetails.procesadorIphone = document.getElementById('procesadorIphone').value;
                productDetails.camaraIphone = document.getElementById('camaraIphone').value;
                productDetails.faceidIphone = document.getElementById('faceidIphone').value;
                productDetails.memoryIphone = document.getElementById('memoryIphone').value;
                productDetails.geolocalizacion = document.getElementById('geolocalizacion').value;
                productDetails.reproduccionIphone = document.getElementById('reproduccionIphone').value;
                productDetails.sensoresIphone = document.getElementById('sensoresIphone').value;
                productDetails.grabacionIphone = document.getElementById('grabacionIphone').value;
                productDetails.siriIphone = document.getElementById('siriIphone').value;
                productDetails.bateriaIphone = document.getElementById('bateriaIphone').value;
                break;

            case 'ipad':
                productDetails.screenSizeIpad = document.getElementById('screenSizeIpad').value;
                productDetails.capacidadIpad = document.getElementById('capacidadIpad').value;
                productDetails.memoriaipad = document.getElementById('memoriaipad').value;
                productDetails.procesadorIpad = document.getElementById('procesadorIpad').value;
                productDetails.camaraIpad = document.getElementById('camaraIpad').value;
                productDetails.softwareIpad = document.getElementById('softwareIpad').value;
                productDetails.conexioninalambricaIpad = document.getElementById('conexioninalambricaIpad').value;
                productDetails.audioIpad = document.getElementById('audioIpad').value;
                productDetails.geolocalizacionIpad = document.getElementById('geolocalizacionIpad').value;
                productDetails.bateriaIpad = document.getElementById('bateriaIpad').value;
                productDetails.sensoresIpad = document.getElementById('sensoresIpad').value;
                productDetails.tuchIdIpad = document.getElementById('tuchIdIpad').value;
                productDetails.siriIpad = document.getElementById('siriIpad').value;
                break;

            case 'airpods':
                productDetails.batteryLifeAirpods = document.getElementById('batteryLifeAirpods').checked;
                productDetails.noiseCancellation = document.getElementById('noiseCancellation').value;
                productDetails.sensoresAirpods = document.getElementById('sensoresAirpods').value;
                break;

            case 'applevisionpro':
                productDetails.screenSiseVision = document.getElementById('screenSiseVision').checked;
                productDetails.batteryVisionPro = document.getElementById('batteryVisionPro').checked;
                productDetails.sensoresVisionPro = document.getElementById('sensoresVisionPro').checked;
                productDetails.modosVisionPro = document.getElementById('modosVisionPro').checked;
                productDetails.juegos = document.getElementById('juegos').checked;
                break;

            case 'watch':
                productDetails.batteryLifewatch = document.getElementById('batteryLifewatch').checked;
                productDetails.sensoreswatch = document.getElementById('sensoreswatch').checked;
                productDetails.modos = document.getElementById('modos').checked;
                break;
        }

        if (editProductId === null) {
            // Agrega el nuevo producto
            products.push(productDetails);
            alert('Producto agregado!');
        } else {
            // Edita el producto existente
            const index = products.findIndex(product => product.id === editProductId);
            products[index] = productDetails;
            alert('Producto editado!');
            editProductId = null; // Restablece el ID de edición
        }

        renderProducts(); // Actualiza la lista de productos
        productModal.style.display = 'none'; // Oculta el modal
    });

    // Función para renderizar la lista de productos
    function renderProducts() {
        productList.innerHTML = ''; // Limpia la lista existente
        products.forEach(product => {
            const card = document.createElement('div');
            card.className = 'product-card';
            card.innerHTML = `
                <input type="checkbox" class="product-checkbox" data-id="${product.id}">
                <img src="${product.image || 'ruta/a/imagen/por/defecto.jpg'}" alt="${product.name}"> <!-- Imagen por defecto -->
                <h3>${product.name}</h3>
                <p>Precio: $${product.price}</p>
                <p>Tipo: ${product.type}</p>
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

        console.log(products); // Verifica que los productos se agregan correctamente al array
    }


    // Función para editar un producto
    function editProduct(productId) {
        const productToEdit = products.find(product => product.id === productId);
        if (productToEdit) {
            document.getElementById('productName').value = productToEdit.name;
            document.getElementById('price').value = productToEdit.price;
            productType.value = productToEdit.type;

            // Muestra campos específicos
            productType.dispatchEvent(new Event('change'));

            // Completa los campos específicos
            switch (productToEdit.type) {
                case 'mac':
                    document.getElementById('screenSizeMac').value = productToEdit.screenSizeMac;
                    document.getElementById('capacidadMac').value = productToEdit.capacidadMac;
                    document.getElementById('memoriaMac').value = productToEdit.memoriaMac;
                    document.getElementById('procesadorMac').value = productToEdit.procesadorMac;
                    document.getElementById('softwareMac').value = productToEdit.softwareMac;
                    document.getElementById('conexionInalambricaMac').value = productToEdit.conexionInalambricaMac;
                    document.getElementById('audioMac').value = productToEdit.audioMac;
                    document.getElementById('tecladoMac').value = productToEdit.tecladoMac;
                    document.getElementById('camaraMac').value = productToEdit.camaraMac;
                    document.getElementById('formatoMac').value = productToEdit.formatoMac;
                    document.getElementById('bateriaMac').value = productToEdit.bateriaMac;
                    break;

                case 'iphone':
                    document.getElementById('screenSizeIphone').value = productToEdit.screenSizeIphone;
                    document.getElementById('resolutionIphone').value = productToEdit.resolutionIphone;
                    document.getElementById('resistenciaIphone').value = productToEdit.resistenciaIphone;
                    document.getElementById('procesadorIphone').value = productToEdit.procesadorIphone;
                    document.getElementById('camaraIphone').value = productToEdit.camaraIphone;
                    document.getElementById('faceidIphone').value = productToEdit.faceidIphone;
                    document.getElementById('memoryIphone').value = productToEdit.memoryIphone;
                    document.getElementById('geolocalizacion').value = productToEdit.geolocalizacion;
                    document.getElementById('reproduccionIphone').value = productToEdit.reproduccionIphone;
                    document.getElementById('sensoresIphone').value = productToEdit.sensoresIphone;
                    document.getElementById('grabacionIphone').value = productToEdit.grabacionIphone;
                    document.getElementById('siriIphone').value = productToEdit.siriIphone;
                    document.getElementById('bateriaIphone').value = productToEdit.bateriaIphone;
                    break;

                case 'ipad':
                    document.getElementById('screenSizeIpad').value = productToEdit.screenSizeIpad;
                    document.getElementById('capacidadIpad').value = productToEdit.capacidadIpad;
                    document.getElementById('memoriaipad').value = productToEdit.memoriaipad;
                    document.getElementById('procesadorIpad').value = productToEdit.procesadorIpad;
                    document.getElementById('camaraIpad').value = productToEdit.camaraIpad;
                    document.getElementById('softwareIpad').value = productToEdit.softwareIpad;
                    document.getElementById('conexioninalambricaIpad').value = productToEdit.conexioninalambricaIpad;
                    document.getElementById('audioIpad').value = productToEdit.audioIpad;
                    document.getElementById('geolocalizacionIpad').value = productToEdit.geolocalizacionIpad;
                    document.getElementById('bateriaIpad').value = productToEdit.bateriaIpad;
                    document.getElementById('sensoresIpad').value = productToEdit.sensoresIpad;
                    document.getElementById('tuchIdIpad').value = productToEdit.tuchIdIpad;
                    document.getElementById('siriIpad').value = productToEdit.siriIpad;
                    break;

                case 'airpods':
                    document.getElementById('batteryLifeAirpods').checked = productToEdit.batteryLifeAirpods;
                    document.getElementById('noiseCancellation').value = productToEdit.noiseCancellation;
                    document.getElementById('sensoresAirpods').value = productToEdit.sensoresAirpods;
                    break;

                case 'applevisionpro':
                    document.getElementById('screenSiseVision').checked = productToEdit.screenSiseVision;
                    document.getElementById('batteryVisionPro').checked = productToEdit.batteryVisionPro;
                    document.getElementById('sensoresVisionPro').checked = productToEdit.sensoresVisionPro;
                    document.getElementById('modosVisionPro').checked = productToEdit.modosVisionPro;
                    document.getElementById('juegos').checked = productToEdit.modosVisionPro;
                    break;

                case 'watch':
                    document.getElementById('batteryLifewatch').checked = productToEdit.batteryLifewatch;
                    document.getElementById('sensoreswatch').checked = productToEdit.sensoreswatch;
                    document.getElementById('modos').checked = productToEdit.modos;
                    break;
            }

            // Muestra el modal con el formulario de edición
            productModal.style.display = 'block';
            editProductId = productId; // Establece el ID del producto que se está editando
            document.getElementById('form-title').textContent = 'Editar Producto';
        }
    }

    // Eliminar productos seleccionados
    deleteSelectedBtn.addEventListener('click', () => {
        const checkboxes = document.querySelectorAll('.product-checkbox:checked');
        checkboxes.forEach(checkbox => {
            const productId = parseInt(checkbox.getAttribute('data-id'));
            products = products.filter(product => product.id !== productId);
        });
        renderProducts(); // Actualiza la lista de productos después de eliminar
    });
});

// Botón para volver arriba
var btnSubir = document.getElementById("btn-subir-arriba");
btnSubir.onclick = function () {
    window.scrollTo({ top: 0, behavior: 'smooth' });
};

window.onscroll = function () {
    if (document.body.scrollTop > 100 || document.documentElement.scrollTop > 100) {
        btnSubir.style.display = "block";
    } else {
        btnSubir.style.display = "none";
    }
};
