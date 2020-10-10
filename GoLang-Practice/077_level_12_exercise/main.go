package main


import "github.com/ShitalBhandare/Programming-Practice/GoLang-Practice/077_level_12_exercise/dog"
import "fmt"


func main() {
	human_years := 3
	// dog_years gets the converted human years to dog years
	dog_years := dog.Years(human_years)
	fmt.Println("Dog Years:",dog_years)

}
