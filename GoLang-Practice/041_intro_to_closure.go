package main

import (
	"fmt"
)

// Closure: Limiting the scope of the variable

var x int					// Package level scope. Accessible anywhere in the program

func main() {
	fmt.Println("x:", x)
	foo()

	y := 2					// Function level scope
	fmt.Println("y:", y)

	{
		z := 42				// Code block level scope
		fmt.Println("z:", z)
	}

	//fmt.Println("z:", z)			// undefined: z error

	a := incrementor()
	b := incrementor()
	fmt.Println(a())			// return: 1
	fmt.Println(a())			// return: 2
	fmt.Println(a())			// return: 3
	fmt.Println(b())			// return: 1		
	fmt.Println(b())			// return: 2

}

func foo() {
	fmt.Println("x in foo():", x)
	//fmt.Println("y", y)			// undefined: y error

}

func incrementor() func () int {
	var i int
	return func() int {
		i++
		return i
	}
}

