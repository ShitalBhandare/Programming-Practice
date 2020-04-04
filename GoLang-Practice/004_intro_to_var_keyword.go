package main

import "fmt"

// Below statement will throw an error as 
// non declaration statement is outside of function body.
//x := 10

// var KEYWORD can be used outside function body.
// its scope is till the end of the program
var z = 30

// DECLARE a IDENTIFIER i with the type INT
// DEFAULT value would be false for booleans, 0 for numeric types, "" for strings, and 
// nil for pointers, functions, interfaces, slices, channels, and maps
var i int

func main() {

	// DECLARE and ASSIGN a identifier = INITIALIZATION
	x := 10
	fmt.Println("x:",x)

	var y = 20
	fmt.Println("y:",y)

	fmt.Println("z:",z)

	foo()

	fmt.Println("i:",i)
}

func foo() {
	fmt.Println("In foo(), z:", z)
}
