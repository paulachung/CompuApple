package main

import "fmt"

func main(){
	type Persona struct{
		Name string
		Age int
	}
	personas := []Persona{
		{"hernan",10},
		{"hernancito", 12},
		{"joselito", 10},
	}
	for _, persona := range personas{
		fmt.Printf("Name: %s, Age: %d\n", persona.Name, persona.Age)
	}
}