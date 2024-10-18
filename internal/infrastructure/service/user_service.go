package service

import (
	"compuApple/internal/business/domain"
	"compuApple/internal/infrastructure/repository"
	"errors"
)

type UserService interface {
	Create(user domain.User) (domain.User, error)
	Validate(credentials domain.UserCredentials) (domain.User, error)
}

type userService struct {
	repo repository.UserRepository
}

func NewUserService(repo repository.UserRepository) UserService {
	return &userService{
		repo: repo,
	}
}

// Método para crear un nuevo usuario
func (s *userService) Create(user domain.User) (domain.User, error) {
	createdUser, err := s.repo.Create(user)
	if err != nil {
		return domain.User{}, err
	}
	return createdUser, nil
}

// Método para validar las credenciales de usuario
func (s *userService) Validate(credentials domain.UserCredentials) (domain.User, error) {
	// Obtener el usuario por su email
	user, err := s.repo.GetByEmail(credentials.Email)
	if err != nil {
		return domain.User{}, errors.New("usuario no encontrado")
	}

	// Verificar si la contraseña coincide
	if user.Password != credentials.Password {
		return domain.User{}, errors.New("contraseña incorrecta")
	}

	return user, nil
}
