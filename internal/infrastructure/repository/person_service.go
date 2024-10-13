package repository

import "compuApple/internal/business/domain"

type PersonService interface{
	Create(person domain.Persona) (domain.PersonDTO, error)
    GetAll() ([]domain.Persona, error)
}