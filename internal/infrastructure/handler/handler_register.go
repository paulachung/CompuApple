package handler

import (
	"compuApple/internal/business/domain"
	"compuApple/internal/infrastructure/service"
	"encoding/json"
	"net/http"
)

type RegisterHandler struct {
    service service.UserService // un servicio que maneje las operaciones de usuario
}

func NewRegisterHandler(service service.UserService) *RegisterHandler {
    return &RegisterHandler{
        service: service,
    }
}

func (h *RegisterHandler) Register() http.HandlerFunc {
    return func(w http.ResponseWriter, r *http.Request) {
        var user domain.User

        // Decodificar el cuerpo de la solicitud
        if err := json.NewDecoder(r.Body).Decode(&user); err != nil {
            w.WriteHeader(http.StatusBadRequest)
            json.NewEncoder(w).Encode(map[string]string{"error": "Datos inválidos"})
            return
        }

        // Crear el usuario
        newUser, err := h.service.Create(user)
        if err != nil {
            w.WriteHeader(http.StatusInternalServerError)
            json.NewEncoder(w).Encode(map[string]string{"error": "Error al crear el usuario"})
            return
        }

        w.WriteHeader(http.StatusCreated)
        json.NewEncoder(w).Encode(newUser)
    }
}
