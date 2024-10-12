package repository

import (
	"compuApple/borrar/internal/business/domain"
	"database/sql"
)

//instancia del repositorio

type PersonRepository struct{
	db *sql.DB//puntero de sql 
}

//constructor  / devuelve una instancia de la estructura personrepository
func PersonRepository(db *sql.DB) *PersonRepository{
	return &PersonRepository{
		db: db,
	}
}

//implementacion de los metodos /repository nos permite acceder a la base de datos
func(repository *PersonRepository) GetAll() ([]domain.Persona, error){
	//execute query
	rows, err := repository.db.Query("SELECT p.id, p.name, p.age FROM persons AS p")
	if err!= nil {
		return nil, err
	}
	//obtener las filas
	persons := []domain.Persona{}
	for rows.Next() {
		//crear una persona
		var person domain.Persona
		//escaneo el valor de las columnas de dicha fila
		err := rows.Scan(&person.DNI, &person.Name, &person.Age)
		if err != nil {
			return nil, err
		}
		persons = append(persons, person)
	}
	errRows := rows.Err()
	if err != nil{
		return nil, errRows
	}
	return persons, nil
}