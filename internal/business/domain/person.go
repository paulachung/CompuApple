package domain

type (
	Persona struct {
		DNI  int    `json:"dni"` //etiquetas entre patics
		Name string `json:"name"`
		Age  int    `json:"age"`
	}
	PersonDTO struct {
		DNI  int    `json:"dni"`
		Name string `json:"name"`
	}
)