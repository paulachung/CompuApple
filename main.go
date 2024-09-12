package main

import (
	"log"
	"net/http"
)

func main() {
	// Sirve los archivos estáticos (CSS, JS, imágenes)
	http.Handle("/static/", http.StripPrefix("/static/", http.FileServer(http.Dir("static"))))

	// Sirve el archivo HTML para la ruta raíz "/"
	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		http.ServeFile(w, r, "templates/index.html")
	})

	// Inicia el servidor en el puerto 8080
	log.Println("Servidor corriendo en http://localhost:8080")
	err := http.ListenAndServe(":8080", nil)
	if err != nil {
		log.Fatal("Error al iniciar el servidor:", err)
	}
}
