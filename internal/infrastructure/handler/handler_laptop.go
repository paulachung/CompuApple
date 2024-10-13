package handler

import (
	"compuApple/internal/business/domain"
	"compuApple/internal/infrastructure/service"
	"encoding/json"
	"net/http"
)

// instancia del handler
type LaptopHandler struct {
	service service.LaptopService
}

func NewLaptopHandler(service service.LaptopService) *LaptopHandler {
	return &LaptopHandler{
		service: service,
	}
}

type CreateLaptopResponse struct {
	Status int    `json:"status"`
	Data   domain.LaptopDTO  `json:"data,omitempty"`
	Error  string `json:"error,omitempty"`
}

func (handler *LaptopHandler) Create() http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		var laptop domain.Laptop

		if err := json.NewDecoder(r.Body).Decode(&laptop); err != nil {
			w.Header().Set("Content-Type", "application/json")
			w.WriteHeader(http.StatusBadRequest) // 400
			response := CreateLaptopResponse{
				Status: http.StatusBadRequest,
				Error:  "invalid request body",
			}
			if err := json.NewEncoder(w).Encode(response); err != nil {
				http.Error(w, "Failed to encode response", http.StatusInternalServerError)
			}
			return
		}

		// procesar los datos
		newLaptop, err := handler.service.Create(laptop)
		if err != nil {
			w.Header().Set("Content-Type", "application/json")
			w.WriteHeader(http.StatusInternalServerError)
			response := CreateLaptopResponse{
				Status: http.StatusInternalServerError,
				Error:  "failed to create laptop",
			}
			if err := json.NewEncoder(w).Encode(response); err != nil {
				http.Error(w, "Failed to encode response", http.StatusInternalServerError)
			}
			return
		}

		// respuesta exitosa
		response := CreateLaptopResponse{
			Status: http.StatusOK,
			Data:   newLaptop,
		}
		w.Header().Set("Content-Type", "application/json")
		w.WriteHeader(http.StatusOK)
		if err := json.NewEncoder(w).Encode(response); err != nil {
			http.Error(w, "Failed to encode response", http.StatusInternalServerError)
		}
	}
}

type GetLaptopsResponse struct {
	Status int    `json:"status"`
	Data   []domain.LaptopDTO `json:"data,omitempty"`
	Error  string `json:"error,omitempty"`
}

func (handler *LaptopHandler) GetAll() http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		// procesar los datos
		laptops, err := handler.service.GetAll()
		if err != nil {
			w.Header().Set("Content-Type", "application/json")
			w.WriteHeader(http.StatusInternalServerError)
			response := GetLaptopsResponse{
				Status: http.StatusInternalServerError,
				Error:  "internal server error has occurred",
			}
			if err := json.NewEncoder(w).Encode(response); err != nil {
				http.Error(w, "Failed to encode response", http.StatusInternalServerError)
			}
			return
		}

		// convertir laptops a DTO
		laptopDTOs := make([]domain.LaptopDTO, len(laptops))
		for i, laptop := range laptops {
			laptopDTOs[i] = domain.LaptopDTO{
				ID:         laptop.ID,
				Modelo:     laptop.Modelo,
				Color:      laptop.Color,
				Medidas:   laptop.Medidas,
				RAM:       laptop.RAM,
				CapacidadAlmacenamiento: laptop.CapacidadAlmacenamiento,
				DuracionBateria:       laptop.DuracionBateria,
				CaracteristicasGenerales: laptop.CaracteristicasGenerales,
			}
		}

		// respuesta exitosa
		response := GetLaptopsResponse{
			Status: http.StatusOK,
			Data:   laptopDTOs,
		}
		w.Header().Set("Content-Type", "application/json")
		w.WriteHeader(http.StatusOK)
		if err := json.NewEncoder(w).Encode(response); err != nil {
			http.Error(w, "Failed to encode response", http.StatusInternalServerError)
		}
	}
}
