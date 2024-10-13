package mainApi

import (
	"log"
	"net/http"
)

func mainApi() {
	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request){
		w.Write([]byte("Pagina de home "))
	})
	log.Println("Ejecutando el servidor en el puerto http://localhost:8000")
	http.ListenAndServe(":8000", nil)
}