package service

import "compuApple/internal/business/domain"

//interfaz con metodos para hacer operaciones con laptops
type LaptopService interface {
	Create(laptop domain.Laptop) (domain.LaptopDTO, error)
	GetAll() ([]domain.LaptopDTO, error)
}
