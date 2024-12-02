function filterProducts(category) {
    const allProducts = document.querySelectorAll('#product-list .card');
    let anyVisible = false;  // Variable para rastrear si hay productos visibles

    allProducts.forEach(product => {
        // Verificar si el producto pertenece a la categoría
        if (product.getAttribute('data-categoria') === category) {
            product.style.display = 'block';  // Mostrar el producto
            anyVisible = true;  // Marcar que hay al menos un producto visible
        } else {
            product.style.display = 'none';  // Ocultar productos que no coinciden
        }
    });

    // Mostrar mensaje si no hay productos visibles
    const noProductsMessage = document.getElementById('no-products-message');
    if (anyVisible) {
        noProductsMessage.style.display = 'none';  // Ocultar el mensaje
    } else {
        noProductsMessage.style.display = 'block';  // Mostrar el mensaje
    }
}

// Función para filtrar por precio
function filterByPrice() {
    // Obtener los valores de precio mínimo y máximo
    const minPrice = parseFloat(document.getElementById('precio-min').value) || 0;
    const maxPrice = parseFloat(document.getElementById('precio-max').value) || Infinity;

    // Seleccionar todos los productos
    const allProducts = document.querySelectorAll('#product-list .card');
    let anyVisible = false;

    allProducts.forEach(product => {
        // Obtener el precio del producto
        const productPrice = parseFloat(product.querySelector('.price').textContent.replace('$', ''));

        // Verificar si el precio está dentro del rango
        if (productPrice >= minPrice && productPrice <= maxPrice) {
            product.style.display = 'block';  // Mostrar el producto
            anyVisible = true;  // Marcar que hay al menos un producto visible
        } else {
            product.style.display = 'none';  // Ocultar productos fuera del rango
        }
    });

    // Mostrar mensaje si no hay productos visibles en el rango de precios
    const noProductsMessage = document.getElementById('no-products-message');
    noProductsMessage.style.display = anyVisible ? 'none' : 'block';
}

// Variable para almacenar la categoría seleccionada
let selectedCategory = null;

function applyFilters(category = null) {
    // Si se recibe una categoría, actualiza la categoría seleccionada
    if (category) {
        selectedCategory = category;
    }

    // Obtener los valores de precio mínimo y máximo
    const minPrice = parseFloat(document.getElementById('precio-min').value) || 0;
    const maxPrice = parseFloat(document.getElementById('precio-max').value) || Infinity;

    // Seleccionar todos los productos
    const allProducts = document.querySelectorAll('#product-list .card');
    let anyVisible = false;

    allProducts.forEach(product => {
        const productCategory = product.getAttribute('data-categoria');
        const productPrice = parseFloat(product.querySelector('.price').textContent.replace('$', ''));

        // Verificar si el producto cumple con el filtro de categoría y el rango de precio
        const categoryMatch = !selectedCategory || productCategory === selectedCategory;
        const priceMatch = productPrice >= minPrice && productPrice <= maxPrice;

        // Mostrar el producto solo si cumple ambos filtros
        if (categoryMatch && priceMatch) {
            product.style.display = 'block';
            anyVisible = true;
        } else {
            product.style.display = 'none';
        }
    });

    // Mostrar el mensaje de "No hay productos disponibles" si no hay productos visibles
    const noProductsMessage = document.getElementById('no-products-message');
    noProductsMessage.style.display = anyVisible ? 'none' : 'block';
}

// Función para mostrar todos los productos (resetea filtros)
function loadAllProducts() {
    selectedCategory = null;  // Restablece la categoría seleccionada
    document.getElementById('precio-min').value = '';
    document.getElementById('precio-max').value = '';

    // Mostrar todos los productos
    const allProducts = document.querySelectorAll('#product-list .card');
    allProducts.forEach(product => {
        product.style.display = 'block';
    });

    // Ocultar el mensaje de "No hay productos disponibles"
    document.getElementById('no-products-message').style.display = 'none';
}

// Función para alternar la visibilidad del menú desplegable de categorías
function toggleDropdown() {
    const dropdown = document.getElementById('dropdown-categorias');
    dropdown.style.display = dropdown.style.display === 'none' ? 'block' : 'none';
}

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

function buscarProducto() {
    const input = document.getElementById('buscar').value.toLowerCase();
    const productos = document.querySelectorAll('.card');
    let encontrados = false; // Bandera para saber si hay productos visibles

    productos.forEach(producto => {
        const nombreProducto = producto.querySelector('.card-title').textContent.toLowerCase();
        if (nombreProducto.includes(input)) {
            producto.style.display = 'block'; // Muestra el producto
            encontrados = true; // Se encontró al menos un producto
        } else {
            producto.style.display = 'none'; // Oculta el producto
        }
    });

    // Muestra o oculta el mensaje de "No se encontraron productos"
    const noResultados = document.getElementById('no-resultados');
    if (encontrados) {
        noResultados.style.display = 'none'; // Oculta el mensaje si hay productos
    } else {
        noResultados.style.display = 'block'; // Muestra el mensaje si no hay productos
    }
}

//carrito//

document.addEventListener("DOMContentLoaded", function () {
    let cartCount = 0;
    const cartCounter = document.getElementById('cart-counter');
    const cartConfirmation = document.getElementById('cart-confirmation');

    // Función para agregar el producto al carrito
    async function addToCart(productId, productName, productPrice) {
        try {
            const response = await fetch('/add-to-cart', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    productId: productId,
                    productName: productName,
                    productPrice: productPrice
                })
            });

            if (response.ok) {
                cartCount++;
                cartCounter.textContent = cartCount;

                // Mostrar mensaje de añadido al carrito
                cartConfirmation.style.display = 'block';
                setTimeout(() => {
                    cartConfirmation.style.display = 'none';
                }, 2000);
            } else {
                console.error('Error al agregar el producto al carrito');
            }
        } catch (error) {
            console.error('Error en la solicitud:', error);
        }
    }

    document.querySelectorAll('.add-to-cart').forEach(button => {
        button.addEventListener('click', function () {
            const productId = this.getAttribute('data-product-id');
            const productName = this.getAttribute('data-product-name');
            const productPrice = this.getAttribute('data-product-price');
            addToCart(productId, productName, productPrice);
        });
    });

    document.querySelectorAll('.buy-now').forEach(button => {
        button.addEventListener('click', function () {
            const productId = this.closest('.card').querySelector('.add-to-cart').getAttribute('data-product-id');
            const productName = this.closest('.card').querySelector('.add-to-cart').getAttribute('data-product-name');
            const productPrice = this.closest('.card').querySelector('.add-to-cart').getAttribute('data-product-price');
            addToCart(productId, productName, productPrice);
        });
    });

});

// Agregar la inicialización de eventos para los botones del menú lateral
document.querySelectorAll('.menu-lateral li').forEach(function (item) {
    item.addEventListener('click', function () {
        const categoria = this.getAttribute('data-category');
        if (categoria) {
            filterProducts(categoria);
        }
    });
});


document.getElementById('cartIcon').addEventListener('click', openCartModal);

async function openCartModal() {
    // Mostrar el modal
    const modal = document.getElementById('cartModal');
    modal.style.display = 'block';

    // Llamada a la API para obtener los productos del carrito
    const response = await fetch('/get-cart-items');
    if (response.ok) {
        const data = await response.json();
        if (data.success) {
            displayCartItems(data.cartItems);
        } else {
            console.error("Error al obtener los productos del carrito:", data.message);
        }
    } else {
        console.error("Error en la solicitud al servidor.");
    }
}

// Función para mostrar los productos en el modal
function displayCartItems(cartItems) {
    const container = document.getElementById('cartItemsContainer');
    container.innerHTML = ''; // Limpiar el contenido previo

    let total = 0;

    cartItems.forEach(item => {
        const itemDiv = document.createElement('div');
        itemDiv.className = 'cart-item';
        itemDiv.innerHTML = `
        <p>${item.product_name}</p>
        <p>Cantidad: ${item.quantity}</p>
        <p>Precio: $${item.product_price}</p>
    `;
        container.appendChild(itemDiv);

        // Calcular el total
        total += item.product_price * item.quantity;
    });

    // Actualizar el total en el modal
    document.getElementById('totalAmount').textContent = total.toFixed(2);
}

// Función para cerrar el modal
function closeCart() {
    const modal = document.getElementById('cartModal');
    modal.style.display = 'none';
}

// Cerrar el modal si se hace clic fuera de él
window.onclick = function (event) {
    const modal = document.getElementById('cartModal');
    if (event.target == modal) {
        modal.style.display = 'none';
    }
};

//check out carrito//
async function checkout() {
    const userConfirmed = confirm("¿Estás seguro de que deseas finalizar la compra?");
    if (!userConfirmed) return; // Salir si el usuario cancela

    // Realiza la solicitud para finalizar la compra
    const response = await fetch('/checkout', {
        method: 'POST'
    });

    if (response.ok) {
        const data = await response.json();
        if (data.success) {
            alert("Compra realizada con éxito. Se ha enviado un correo de confirmación.");
            closeCart(); // Cierra el modal después de finalizar la compra
        } else {
            alert("Error al finalizar la compra: " + data.message);
        }
    } else {
        console.error("Error en la solicitud al servidor.");
    }
}

//VACIAR carrito//
async function emptyCart() {
    const userConfirmed = confirm("¿Estás seguro de que deseas vaciar el carrito?");
    if (!userConfirmed) return; // Salir si el usuario cancela

    const response = await fetch('/empty-cart', {
        method: 'POST'
    });

    if (response.ok) {
        const data = await response.json();
        if (data.success) {
            alert("El carrito ha sido vaciado.");
            displayCartItems([]); // Limpia la vista del carrito
            document.getElementById('totalAmount').textContent = "0"; // Reinicia el total
            document.getElementById('cart-counter').textContent = "0"; // Reinicia el contador en el icono del carrito
        } else {
            alert("Error al vaciar el carrito: " + data.message);
        }
    } else {
        console.error("Error en la solicitud al servidor.");
    }
}

function renderCartItems(cartItems) {
    let cartContainer = document.getElementById('cartContainer');
    cartContainer.innerHTML = ''; // Limpia el contenido actual

    let total = 0;
    let uniqueItems = {};

    cartItems.forEach(item => {
        if (uniqueItems[item.product_id]) {
            uniqueItems[item.product_id].quantity += item.quantity;
        } else {
            uniqueItems[item.product_id] = item;
        }
    });

    Object.values(uniqueItems).forEach(item => {
        let itemElement = document.createElement('div');
        itemElement.className = 'cart-item';

        // Nombre del producto
        let nameElement = document.createElement('p');
        nameElement.textContent = item.product_name;

        // Input para cantidad
        let quantityInput = document.createElement('input');
        quantityInput.type = 'number';
        quantityInput.value = item.quantity;
        quantityInput.min = 1;
        quantityInput.oninput = () => updateCartItem(item.product_id, quantityInput.value);

        // Precio del producto
        let priceElement = document.createElement('p');
        priceElement.textContent = `Precio: $${item.product_price.toFixed(2)}`;

        // Botón de eliminar
        let removeButton = document.createElement('button');
        removeButton.textContent = 'Eliminar';
        removeButton.onclick = () => removeFromCart(item.product_id);

        // Agregar elementos al contenedor del producto
        itemElement.appendChild(nameElement);
        itemElement.appendChild(quantityInput);
        itemElement.appendChild(priceElement);
        itemElement.appendChild(removeButton);

        cartContainer.appendChild(itemElement);

        // Calcular el total
        total += item.product_price * item.quantity;
    });

    let totalElement = document.createElement('p');
    totalElement.id = 'total';
    totalElement.textContent = `Total: $${total.toFixed(2)}`;
    cartContainer.appendChild(totalElement);
}


//eliminar un producto del carrito
function removeFromCart(productId) {
    fetch('/remove-from-cart', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ productId: productId })
    })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                getCartItems(); // Refresca el carrito después de eliminar el producto
            } else {
                alert('Error: ' + data.message);
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
}



// actualizar cantidad de un producto
function updateCartItem(productId, newQuantity) {
    if (newQuantity < 1) {
        alert('La cantidad debe ser al menos 1');
        return;
    }

    fetch('/update-cart-item', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ productId: productId, newQuantity: parseInt(newQuantity) })
    })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                getCartItems(); // Refresca el carrito después de actualizar la cantidad
            } else {
                alert('Error: ' + data.message);
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
}


document.addEventListener('DOMContentLoaded', getCartItems);


function getCartItems() {
    fetch('/get-cart-items')
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                // Renderiza los productos en el carrito
                renderCartItems(data.cartItems);
            } else {
                alert('Error al obtener los productos del carrito');
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
}


