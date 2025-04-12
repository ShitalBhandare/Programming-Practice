package main

import "fmt"

type my_var int
var x my_var
var y int

func main() {

        fmt.Println("x: ", x)
        fmt.Printf("Type of variable x: %T\n", x)
        x = 42
        fmt.Println("After assignment x:", x)
	y = int(x)
	fmt.Println("y: ", y)
        fmt.Printf("Type of variable y: %T\n", y)

}

============OUTPUT==================

x:  0
Type of variable x: main.my_var
After assignment x: 42
y:  42
Type of variable y: int
