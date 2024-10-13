package service

import (
	"compuApple/internal/business/domain"
	"compuApple/internal/infrastructure/repository"
)

type laptopService struct {
	repo repository.LaptopRepository
}

func NewLaptopService(repo repository.LaptopRepository) LaptopService {
	return &laptopService{
		repo: repo,
	}
}

func (s *laptopService) Create(laptop domain.Laptop) (domain.LaptopDTO, error) {
	// Aquí puedes incluir la lógica para crear la laptop en la base de datos
	createdLaptop, err := s.repo.Create(laptop)
	if err != nil {
		return domain.LaptopDTO{}, err
	}
	return domain.LaptopDTO{
		ID:                     createdLaptop.ID,
		Modelo:                 createdLaptop.Modelo,
		Color:                  createdLaptop.Color,
		Medidas:               createdLaptop.Medidas,
		RAM:                   createdLaptop.RAM,
		CapacidadAlmacenamiento: createdLaptop.CapacidadAlmacenamiento,
		DuracionBateria:       createdLaptop.DuracionBateria,
		CaracteristicasGenerales: createdLaptop.CaracteristicasGenerales,
	}, nil
}

func (s *laptopService) GetAll() ([]domain.LaptopDTO, error) {
	// Aquí puedes incluir la lógica para obtener todas las laptops de la base de datos
	laptops, err := s.repo.GetAll()
	if err != nil {
		return nil, err
	}

	laptopDTOs := make([]domain.LaptopDTO, len(laptops))
	for i, laptop := range laptops {
		laptopDTOs[i] = domain.LaptopDTO{
			ID:                     laptop.ID,
			Modelo:                 laptop.Modelo,
			Color:                  laptop.Color,
			Medidas:               laptop.Medidas,
			RAM:                   laptop.RAM,
			CapacidadAlmacenamiento: laptop.CapacidadAlmacenamiento,
			DuracionBateria:       laptop.DuracionBateria,
			CaracteristicasGenerales: laptop.CaracteristicasGenerales,
		}
	}
	return laptopDTOs, nil
}
