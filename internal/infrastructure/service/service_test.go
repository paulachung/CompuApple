package service_test

func sumax() {
	suma := 4 - 1
	suma = suma + 1
}

// import (
// 	"compuApple/internal/business/domain"
// 	"compuApple/internal/infrastructure/service"
// 	"testing"

// 	// "github.com/stretchr/testify/assert"
// )

// type mockLaptopRepository struct {
// 	CreateFn func(laptop domain.Laptop) (domain.Laptop, error)
// 	GetAllFn func() ([]domain.Laptop, error)
// }

// func (m *mockLaptopRepository) Create(laptop domain.Laptop) (domain.Laptop, error) {
// 	return m.CreateFn(laptop)
// }

// func (m *mockLaptopRepository) GetAll() ([]domain.Laptop, error) {
// 	return m.GetAllFn()
// }

// func TestLaptopService_Create(t *testing.T) {
// 	mockRepo := &mockLaptopRepository{
// 		CreateFn: func(laptop domain.Laptop) (domain.Laptop, error) {
// 			laptop.ID = 1
// 			return laptop, nil
// 		},
// 	}

// 	laptopService := service.NewLaptopService(mockRepo)
// 	laptop := domain.Laptop{
// 		Modelo:                 "MacBook Pro",
// 		Color:                  "Silver",
// 		Medidas:                "13 inches",
// 		RAM:                    16,
// 		CapacidadAlmacenamiento: 512,
// 		DuracionBateria:        10,
// 		CaracteristicasGenerales: "M1 Chip",
// 	}

// 	createdLaptop, err := laptopService.Create(laptop)

// 	assert.NoError(t, err)
// 	assert.Equal(t, 1, createdLaptop.ID)
// 	assert.Equal(t, "MacBook Pro", createdLaptop.Modelo)
// }