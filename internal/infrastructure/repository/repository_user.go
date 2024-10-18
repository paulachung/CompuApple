package repository

import (
	"compuApple/internal/business/domain"
	"database/sql"
	"fmt"
)

type UserRepository interface {
	Create(user domain.User) (*domain.User, error)
}

type userRepository struct {
	db *sql.DB
}

func NewUserRepository(db *sql.DB) UserRepository {
	return &userRepository{db: db}
}

func (r *userRepository) Create(user domain.User) (*domain.User, error) {
	query := "INSERT INTO users (name, email, direccion, telefono, password) VALUES (?, ?, ?, ?, ?)"
	result, err := r.db.Exec(query, user.Name, user.Email, user.Direccion, user.Telefono, user.Password)
	if err != nil {
		return nil, fmt.Errorf("error al crear el usuario: %w", err)
	}

	id, err := result.LastInsertId()
	if err != nil {
		return nil, fmt.Errorf("error al obtener el ID del usuario creado: %w", err)
	}

	user.ID = id
	return &user, nil
}
