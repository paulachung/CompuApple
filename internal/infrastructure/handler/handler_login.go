// verificar que el usuario esta en la bd
package handler

import (
	"compuApple/internal/business/domain"
	"compuApple/internal/infrastructure/service"
	"encoding/json"
	"net/http"
)

type LoginHandler struct {
	service service.UserService
}

func NewLoginHandler(service service.UserService) *LoginHandler {
	return &LoginHandler{
		service: service,
	}
}

func (h *LoginHandler) Login() http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		var credentials domain.UserCredentials

		if err := json.NewDecoder(r.Body).Decode(&credentials); err != nil {
			w.WriteHeader(http.StatusBadRequest)
			json.NewEncoder(w).Encode(map[string]string{"error": "Credenciales inválidas"})
			return
		}

		// Validar las credenciales
		validUser, err := h.service.Validate(credentials)
		if err != nil {
			w.WriteHeader(http.StatusUnauthorized)
			json.NewEncoder(w).Encode(map[string]string{"error": "Usuario o contraseña incorrectos"})
			return
		}

		json.NewEncoder(w).Encode(validUser)
	}
} 

// package handler

// import (
// 	"compuApple/internal/business/domain"
// 	"encoding/json"
// 	"net/http"
// )

// type LoginHandler struct {
//     service UserService // Servicio para validar usuarios
// }

// func NewLoginHandler(service UserService) *LoginHandler {
//     return &LoginHandler{
//         service: service,
//     }
// }

// // Verificar que el usuario está en la base de datos
// func (h *LoginHandler) Login() http.HandlerFunc {
//     return func(w http.ResponseWriter, r *http.Request) {
//         var credentials domain.UserCredentials

//         // Decodificar las credenciales desde el cuerpo de la solicitud
//         if err := json.NewDecoder(r.Body).Decode(&credentials); err != nil {
//             w.WriteHeader(http.StatusBadRequest)
//             json.NewEncoder(w).Encode(map[string]string{"error": "Credenciales inválidas"})
//             return
//         }

//         // Validar las credenciales usando el servicio
//         validUser, err := h.service.Validate(credentials)
//         if err != nil {
//             w.WriteHeader(http.StatusUnauthorized)
//             json.NewEncoder(w).Encode(map[string]string{"error": "Usuario o contraseña incorrectos"})
//             return
//         }

//         // Responder con el usuario validado
//         json.NewEncoder(w).Encode(validUser)
//     }
// }
