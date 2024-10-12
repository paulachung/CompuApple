package domain

type (
	Persona struct {
		DNI  int    `json:"dni"` //etiquetas entre patics
		Name string `json:"name"`
		Age  int    `json:"age"`
	}
)