package main

import "fmt"

type my_var int
var x my_var

func main() {
	fmt.Println("x: ", x)
	fmt.Printf("Type of variable x: %T\n", x)
	x = 42
	fmt.Println("After assignment x:", x)
}
