function mostrarFormulario(){
  const producto = document.getElementById("producto").value
  const formularioDiv = document.getElementById("formulario")

  let formularioHTML = ''

  if (producto == 'iphone'){
    formularioHTML= `
    <div class='formulario'>
      <h2>Formulario iPhone</h2>
      <label>Modelo:</label>
      <input type="text" placeholder="Modelo del iPhone">
      <label>Color:</label>
      <input type="text" placeholder="Color del iPhone">
    </div>
    `
  }else if( producto === 'ipad'){
    formularioHTML= `
      <div class="formulario">
        <h2>Formulario iPad</h2>
        <label>Capacidad:</label>
        <input type="text" placeholder="Capacidad del iPad">
        <label>Color:</label>
        <input type="text" placeholder="Color del iPad">
      </div>
    `
  } else if (producto === 'macbook'){
    formularioHTML = `
      <div class="formulario">
        <h2>Formulario MacBook</h2>
        <label>Modelo:</label>
        <input type="text" placeholder="Modelo de la MacBook">
        <label>Almacenamiento:</label>
        <input type="text" placeholder="Almacenamiento de la MacBook">
      </div>
    `;
  }

  formularioDiv.innerHTML = formularioHTML
}