package main

import (
	"net/http"
)

func main() {
	// static
	fs := http.FileServer(http.Dir("./static"))

	// Solicitudes HTTP
	http.Handle("/", fs)

	// Definir puerto
	port := ":8080"
	println("Servidor escuchando en el puerto", port)

	// Iniciar servidor
	err := http.ListenAndServe(port, nil)
	if err != nil {
		panic(err)
	}
}
