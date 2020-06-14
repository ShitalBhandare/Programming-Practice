package main

import (
	"fmt"
)

// Everything in GO is PASS BY VALUE.
// when we pass a memory address, we are passing a value

func main() {

	// Intro to pointers

	x := 19
	fmt.Println(x)
	fmt.Println(&x)					// & gives the address of a varible

	// int and *int are two different types
	fmt.Printf("Type of x:%T\n", x)			// type: int

	// type: *int =>  *int -- the * is part of the type -- x is of type *int
	// x is a pointer to address where int is stored.
	fmt.Printf("Type of &x:%T\n", &x)

	// Dereferencing
	y := &x						// y points to the same memory location pointed by x
	fmt.Println(*y)					// * gives a value stored at address
	fmt.Println(y)
	fmt.Println(*&x)

	*y = 1995
	fmt.Println(x)					// changing y's value will change x value as well

	// Passing address of variable as an argument to func
	a := 42
	fmt.Println("a befor:", a)
	passing_address(&a)
	fmt.Println("a after:", a)
}


func passing_address(b *int) {
	fmt.Println("b befor:", *b)
	*b = 60
	fmt.Println("b after:", *b)
}
