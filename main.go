package main

import (
<<<<<<< HEAD
	"context"
	"database/sql"
	"fmt"
	"log"

	_ "github.com/go-sql-driver/mysql"
)

// Definimos la estructura Laptop que representa la tabla 'laptop'
type Laptop struct {
    ID                      int64
    Modelo                  string
    Color                   string
    Medidas                 string
    RAM                     string
    CapacidadAlmacenamiento string
    CaracteristicasGenerales string
}

func main() {
    ctx := context.Background()
    db, err := createConnection()
    if err != nil {
        log.Fatal("Error al crear la conexión:", err)
    }
    defer db.Close()

    // Crear una nueva laptop
    nuevaLaptop := Laptop{
        Modelo:                  "Modelo nuevo",
        Color:                   "Negro",
        Medidas:                 "30x20x2 cm",
        RAM:                     "16GB",
        CapacidadAlmacenamiento: "512GB SSD",
        CaracteristicasGenerales: "Pantalla táctil, Teclado retroiluminado",
    }

    id, err := createLaptop(ctx, db, nuevaLaptop)
    if err != nil {
        log.Fatal("Error al crear la laptop:", err)
    }
    fmt.Println("Laptop creada con ID:", id)

    // Obtener una laptop por ID
    laptop, err := getLaptopByID(ctx, db, id)
    if err != nil {
        log.Fatal("Error al obtener la laptop:", err)
    }
    fmt.Printf("Laptop obtenida: %+v\n", laptop)

    // Actualizar la laptop
    laptop.Color = "Plata"
    err = updateLaptop(ctx, db, laptop)
    if err != nil {
        log.Fatal("Error al actualizar la laptop:", err)
    }
    fmt.Println("Laptop actualizada.")

    // Eliminar la laptop
    err = deleteLaptop(ctx, db, id)
    if err != nil {
        log.Fatal("Error al eliminar la laptop:", err)
    }
    fmt.Println("Laptop eliminada.")
}

// Función para crear la conexión a la base de datos
func createConnection() (*sql.DB, error) {
    connectionString := "root:@tcp(localhost:3307)/tecnologia?parseTime=true"
    db, err := sql.Open("mysql", connectionString)
    if err != nil {
        return nil, err
    }

    db.SetMaxOpenConns(5)

    err = db.Ping()
    if err != nil {
        return nil, err
    }
    return db, nil
}

// Función para crear una nueva laptop
func createLaptop(ctx context.Context, db *sql.DB, laptop Laptop) (int64, error) {
    query := `
        INSERT INTO laptop (modelo, color, medidas, ram, capacidad_almacenamiento, caracteristicas_generales)
        VALUES (?, ?, ?, ?, ?, ?)
    `
    result, err := db.ExecContext(ctx, query,
        laptop.Modelo,
        laptop.Color,
        laptop.Medidas,
        laptop.RAM,
        laptop.CapacidadAlmacenamiento,
        laptop.CaracteristicasGenerales,
    )
    if err != nil {
        return 0, err
    }
    id, err := result.LastInsertId()
    if err != nil {
        return 0, err
    }
    return id, nil
}

// Función para obtener una laptop por ID
func getLaptopByID(ctx context.Context, db *sql.DB, id int64) (Laptop, error) {
    query := `
        SELECT id, modelo, color, medidas, ram, capacidad_almacenamiento, caracteristicas_generales
        FROM laptop
        WHERE id = ?
    `
    row := db.QueryRowContext(ctx, query, id)

    var laptop Laptop
    err := row.Scan(
        &laptop.ID,
        &laptop.Modelo,
        &laptop.Color,
        &laptop.Medidas,
        &laptop.RAM,
        &laptop.CapacidadAlmacenamiento,
        &laptop.CaracteristicasGenerales,
    )
    if err != nil {
        if err == sql.ErrNoRows {
            return laptop, fmt.Errorf("no se encontró la laptop con ID %d", id)
        }
        return laptop, err
    }
    return laptop, nil
}

// Función para actualizar una laptop existente
func updateLaptop(ctx context.Context, db *sql.DB, laptop Laptop) error {
    query := `
        UPDATE laptop
        SET modelo = ?, color = ?, medidas = ?, ram = ?, capacidad_almacenamiento = ?, caracteristicas_generales = ?
        WHERE id = ?
    `
    _, err := db.ExecContext(ctx, query,
        laptop.Modelo,
        laptop.Color,
        laptop.Medidas,
        laptop.RAM,
        laptop.CapacidadAlmacenamiento,
        laptop.CaracteristicasGenerales,
        laptop.ID,
    )
    return err
}

// Función para eliminar una laptop por ID
func deleteLaptop(ctx context.Context, db *sql.DB, id int64) error {
    query := `DELETE FROM laptop WHERE id = ?`
    _, err := db.ExecContext(ctx, query, id)
    return err
}


// package main

// import (
// "html/template"
// "net/http"
// )

// func renderTemplate(w http.ResponseWriter, tmpl string, data interface{}) {
// templates := template.Must(template.ParseFiles(
// "templates/index.html",
// "templates/partials/head.html",
// ))
// templates.ExecuteTemplate(w, tmpl, data)
// }

// func homeHandler(w http.ResponseWriter, r *http.Request) {
// data := map[string]interface{}{
// "Title": "CompuApple",
// }
// renderTemplate(w, "index.html", data)
// }

// func main() {
// http.Handle("/static/", http.StripPrefix("/static/", http.FileServer(http.Dir("static"))))
// http.HandleFunc("/", homeHandler)
// http.ListenAndServe(":8080", nil)
// }
=======
	"net/http"
)

func main() {
	// static
	fs := http.FileServer(http.Dir("./static"))

	// Solicitudes HTTP
	http.Handle("/", fs)

	// Definir puerto
	port := ":8080"
	println("Servidor escuchando en el puerto", port)

	// Iniciar servidor
	err := http.ListenAndServe(port, nil)
	if err != nil {
		panic(err)
	}
}
>>>>>>> b5a86c2ba6ea76aaeb42e3b8a442beb0adc3908a
