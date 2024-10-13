package service

import (
	"compuApple/internal/business/domain"
	"errors"
)

var (
	ErrInternalServerError = errors.New("server: internal server error")
)

type PersonServiceInterface interface {
	GetAll() ([]domain.Persona, error) 
	Create(person domain.Persona) (domain.PersonDTO, error) // Puedes mantener este método
}