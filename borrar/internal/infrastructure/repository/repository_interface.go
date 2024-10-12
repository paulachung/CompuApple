package repository

import "compuApple/borrar/internal/business/domain"

type (//todos los metodos del repositorio aca
	PersonRepositoryInterface interface {
		GetAll() ([]domain.Persona, error) //obtener los productos de la bd y devuelve una lista de domain.Person
    Create(domain.Persona) (domain.Persona, error)
    DeleteByDNI(DNI string) error
	}
)