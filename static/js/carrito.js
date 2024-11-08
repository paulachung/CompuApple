let carrito = [];
let subtotal = 0;

function agregarAlCarrito(nombre, precio) {
    carrito.push({ nombre, precio });
    subtotal += precio;
    actualizarCarrito();
}

function eliminarDelCarrito(index) {
    subtotal -= carrito[index].precio;
    carrito.splice(index, 1);
    actualizarCarrito();
}

function vaciarCarrito() {
    carrito = [];
    subtotal = 0;
    actualizarCarrito();
}

function actualizarCarrito() {
    const carritoContainer = document.getElementById('carrito');
    carritoContainer.innerHTML = '';
    
    carrito.forEach((item, index) => {
        const itemDiv = document.createElement('div');
        itemDiv.className = 'carrito-item';
        itemDiv.innerHTML = `
            ${item.nombre} - $${item.precio.toFixed(2)}
            <button onclick="eliminarDelCarrito(${index})">Eliminar</button>
        `;
        carritoContainer.appendChild(itemDiv);
    });
    
    document.getElementById('subtotal').textContent = `Subtotal: $${subtotal.toFixed(2)}`;
    document.getElementById('total').textContent = `Total: $${subtotal.toFixed(2)}`;
}

function comprar() {
    if (carrito.length === 0) {
        alert("El carrito está vacío.");
    } else {
        alert("Compra realizada. ¡Gracias por tu compra!");
        vaciarCarrito();
    }
}
