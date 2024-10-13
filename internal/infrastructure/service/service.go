package service

import (
	"compuApple/internal/business/domain"
	"compuApple/internal/infrastructure/repository"
)

// Instancia del servicio
type DefaultPersonService struct { // Cambiado el nombre a DefaultPersonService
	repository repository.PersonRepository
}

// Constructor
func NewPersonService(repository repository.PersonRepository) *DefaultPersonService { // Actualiza el tipo de retorno
	return &DefaultPersonService{
		repository: repository,
	}
}

// Implementación
func (service *DefaultPersonService) GetAll() ([]domain.Persona, error) {
	// Llamamos al repository
	persons, err := service.repository.GetAll()
	if err != nil {
		return nil, ErrInternalServerError
	}
	return persons, nil
}

// package service

// import (
// 	"compuApple/internal/business/domain"
// 	"compuApple/internal/infrastructure/repository"
// )

// //instancia del servidor
// type PersonService struct{
// 	repository repository.PersonRepository
// }

// //constructor
// func NewPersonService(repository repository.PersonRepository) *PersonService{
// 	return &PersonService{
// 		repository: repository,
// 	}
// }

// //implementacion
// func(service *PersonService) GetAll() ([]domain.Persona, error){
// 	//llamamos al repository
// 	persons, err := service.repository.GetAll()
// 	if(err != nil){
// 		err := ErrInternalServerError
// 		return nil, err
// 	}
// 	return persons, nil
// }