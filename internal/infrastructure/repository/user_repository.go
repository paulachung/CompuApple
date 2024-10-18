package repository

import (
	"compuApple/internal/business/domain"
	"database/sql"
)

type UserRepository interface {
	Create(user domain.User) (domain.User, error)
	GetByEmail(email string) (domain.User, error)
}

type userRepository struct {
	db *sql.DB
}

func NewUserRepository(db *sql.DB) UserRepository {
	return &userRepository{
		db: db,
	}
}

// Crear un nuevo usuario en la base de datos
func (r *userRepository) Create(user domain.User) (domain.User, error) {
	// Lógica para insertar el usuario en la base de datos
	_, err := r.db.Exec("INSERT INTO users (name, email, password) VALUES (?, ?, ?)", user.Name, user.Email, user.Password)
	if err != nil {
		return domain.User{}, err
	}
	return user, nil
}

// Obtener un usuario por su email
func (r *userRepository) GetByEmail(email string) (domain.User, error) {
	var user domain.User
	err := r.db.QueryRow("SELECT id, name, email, password FROM users WHERE email = ?", email).Scan(&user.ID, &user.Name, &user.Email, &user.Password)
	if err != nil {
		if err == sql.ErrNoRows {
			return domain.User{}, nil
		}
		return domain.User{}, err
	}
	return user, nil
}

// package repository

// import (
// 	"compuApple/internal/business/domain"
// 	"database/sql"
// )

// type UserRepository interface {
// 	Create(user domain.User) (domain.User, error)
// }

// type userRepository struct {
// 	db *sql.DB
// }

// func NewUserRepository(db *sql.DB) UserRepository {
// 	return &userRepository{
// 		db: db,
// 	}
// }

// func (r *userRepository) Create(user domain.User) (domain.User, error) {
// 	// Inserción en la base de datos
// 	query := "INSERT INTO users (name, email, address, phone, password) VALUES (?, ?, ?, ?, ?)"
// 	_, err := r.db.Exec(query, user.Name, user.Email, user.Address, user.Phone, user.Password)
// 	if err != nil {
// 		return domain.User{}, err
// 	}
// 	return user, nil
// }