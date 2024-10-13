package repository

import (
	"compuApple/internal/business/domain"
)

// interfaz que define los métodos para acceder a los datos de laptops.
type LaptopRepository interface {
    Create(laptop domain.Laptop) (domain.Laptop, error)       // Método para crear una nueva laptop
    GetAll() ([]domain.Laptop, error)                         // Método para obtener todas las laptops
}