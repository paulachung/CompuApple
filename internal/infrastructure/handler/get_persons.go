package handler

import (
	"compuApple/internal/business/domain"
	"compuApple/internal/infrastructure/service"
	"encoding/json"
	"net/http"
)

type PersonHandler struct {
	service service.PersonService
}

// Constructor para PersonHandler
func NewPersonHandler(service service.PersonService) *PersonHandler {
	return &PersonHandler{
		service: service,
	}
}

// Método para obtener todas las personas
func (handler *PersonHandler) GetAll() http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		// Procesar la solicitud
		persons, err := handler.service.GetAll()
		if err != nil {
			w.Header().Set("Content-Type", "application/json")
			switch {
			case err == service.ErrInternalServerError: 
				w.WriteHeader(http.StatusInternalServerError) // 500
				w.Write([]byte("internal server error has occurred"))
				return
			default:
				w.WriteHeader(http.StatusInternalServerError) // 500
				w.Write([]byte("an unexpected error has occurred"))
				return
			}
		}

		personDTO := make([]domain.PersonDTO, 0)
		for _, person := range persons {
			personDTO = append(personDTO, domain.PersonDTO{
				DNI:  person.DNI,
				Name: person.Name,
			})
		}

		// Respuesta
		response := PersonsResponse{Data: personDTO, Status: http.StatusOK}

		// Serializar a JSON
		w.Header().Set("Content-Type", "application/json")
		w.WriteHeader(http.StatusOK) // 200

		// Serializa la respuesta a JSON y escribe en el responseWriter
		if err := json.NewEncoder(w).Encode(response); err != nil {
			http.Error(w, "Failed to encode response", http.StatusInternalServerError)
		}
	}
}

// Definición del tipo de respuesta
type PersonsResponse struct {
	Status int                `json:"status"`
	Data   []domain.PersonDTO `json:"data"`
	Error  string             `json:"error,omitempty"`
}
