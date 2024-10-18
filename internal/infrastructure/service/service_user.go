// validar los datos antes de guardarlos
package service

import (
	"compuApple/internal/business/domain"
	"compuApple/internal/infrastructure/repository"
	"fmt"
)

type UserService interface {
	Create(user domain.User) (*domain.User, error)
}

type userService struct {
	repo repository.UserRepository
}

func NewUserService(repo repository.UserRepository) UserService {
	return &userService{repo: repo}
}

func (s *userService) Create(user domain.User) (*domain.User, error) {
	// Aquí puedes validar los datos antes de pasarlos al repositorio
	if user.Name == "" || user.Email == "" || user.Password == "" {
		return nil, fmt.Errorf("nombre, email y contraseña son obligatorios")
	}

	// Llamar al repositorio para guardar el usuario
	return s.repo.Create(user)
}
