package handler

import (
	"compuApple/internal/business/domain"
	"compuApple/internal/infrastructure/service"
	"encoding/json"
	"net/http"
)

// instancia del handler
type PostPersonHandler struct {
	service service.PersonService
}

func NewPostPersonHandler(service service.PersonService) *PostPersonHandler {
	return &PostPersonHandler{
		service: service,
	}
}

type CreatePersonResponse struct {
	Status int             `json:"status"`
	Data   domain.PersonDTO `json:"data,omitempty"`
	Error  string          `json:"error,omitempty"`
}

// Cambiar el receptor de la función de 'PersonHandler' a 'PostPersonHandler'
func (handler *PostPersonHandler) Create() http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		var person domain.Persona

		if err := json.NewDecoder(r.Body).Decode(&person); err != nil {
			w.Header().Set("Content-Type", "application/json")
			w.WriteHeader(http.StatusBadRequest) // 400
			response := CreatePersonResponse{
				Status: http.StatusBadRequest,
				Error:  "invalid request body",
			}
			if err := json.NewEncoder(w).Encode(response); err != nil {
				http.Error(w, "Failed to encode response", http.StatusInternalServerError)
			}
			return
		}

		// Procesar los datos
		newPerson, err := handler.service.Create(person)
		if err != nil {
			w.Header().Set("Content-Type", "application/json")
			w.WriteHeader(http.StatusInternalServerError) // 500
			response := CreatePersonResponse{
				Status: http.StatusInternalServerError,
				Error:  "could not create person",
			}
			if err := json.NewEncoder(w).Encode(response); err != nil {
				http.Error(w, "failed to encode response", http.StatusInternalServerError)
			}
			return
		}

		response := CreatePersonResponse{
			Status: http.StatusCreated,
			Data:   newPerson,
		}
		w.Header().Set("Content-Type", "application/json")
		w.WriteHeader(http.StatusCreated) // 201
		if err := json.NewEncoder(w).Encode(response); err != nil {
			http.Error(w, "failed to encode response", http.StatusInternalServerError)
		}
	}
}

// import (
// 	"compuApple/internal/business/domain"
// 	"compuApple/internal/infrastructure/service"
// 	"encoding/json"
// 	"net/http"
// )

// //instancia del handler
// type PostPersonHandler struct{
// 	service service.PersonService
// }

// func NewPostPersonHandler(service service.PersonService) *PostPersonHandler {
// 	return &PostPersonHandler{
// 		service: service,
// 	}
// }

// type CreatePersonResponse struct{
// 	Status int `json:"status"`
// 	Data domain.PersonDTO `json:"data,omitempty"`
// 	Error string `json:"error,omitempty"`
// }

// func (handler *PostPersonHandler) Create() http.HandlerFunc {
// 	return func(w http.ResponseWriter, r *http.Request){
// 		var person domain.Persona

// 		if err := json.NewDecoder(r.Body).Decode(&person); err != nil{
// 			w.Header().Set("Content-Type", "application/json")
// 			w.WriteHeader(http.StatusBadRequest)//400
// 			response := CreatePersonResponse{
// 				Status: http.StatusBadRequest,
// 				Error: "invalid request body",
// 			}
// 			if err := json.NewEncoder(w).Encode(response); err != nil{
// 				http.Error(w, "Failed to encode response", http.StatusInternalServerError)
// 			}
// 			return
// 		}
// 		//procesar los datos
// 		newPerson, err := handler.service.Create(person)
// 		if err != nil{
// 			w.Header().Set("Content-Type","application/json")
// 			return
// 		}
// 		response := CreatePersonResponse{
// 			Status: http.StatusCreated,
// 			Data: newPerson,
// 		}
// 		w.Header().Set("Content-Type","application/json")
// 		w.WriteHeader(http.StatusCreated)//201
// 		if err := json.NewEncoder(w).Encode(response); err != nil{
// 			http.Error(w, "failed to encode response ", http.StatusInternalServerError)
// 		}
// 	}
// }