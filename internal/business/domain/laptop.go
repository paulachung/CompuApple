package domain

type Laptop struct {
	ID                       int    `json:"id"`
	Modelo                   string `json:"modelo"`
	Color                    string `json:"color"`
	Medidas                  string `json:"medidas"`
	RAM                      string `json:"ram"`
	CapacidadAlmacenamiento  string `json:"capacidad_almacenamiento"`
	DuracionBateria          string `json:"duracion_bateria"`
	CaracteristicasGenerales string `json:"caracteristicas_generales"`
}

type LaptopDTO struct {
	ID                       int    `json:"id"`
	Modelo                   string `json:"modelo"`
	Color                    string `json:"color"`
	Medidas                  string `json:"medidas"`
	RAM                      string `json:"ram"`
	CapacidadAlmacenamiento  string `json:"capacidad_almacenamiento"`
	DuracionBateria          string `json:"duracion_bateria"`
	CaracteristicasGenerales string `json:"caracteristicas_generales"`
}
