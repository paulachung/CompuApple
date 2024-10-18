package domain

type User struct {
	ID       int    `json:"id"`
	Name     string `json:"name"`
	Email    string `json:"email"`
	Password string `json:"password"`
}

type UserCredentials struct {
	Email    string `json:"email"`
	Password string `json:"password"`
}

// package domain

// //para registrarse
// type User struct {
// 	ID       int    `json:"id,omitempty"` // ID puede omitirse en el registro
// 	Name     string `json:"name"`
// 	Email    string `json:"email"`
// 	Address  string `json:"address"`
// 	Phone    string `json:"phone"`
// 	Password string `json:"password"`
// }