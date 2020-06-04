package main

import (
	"fmt"
)

func main() {

	// returning a string from a function
	s := foo()
	fmt.Println(s)

	// returning a function from a function
	x := bar()
	fmt.Printf("%T\n", x)				// Its type is func. Function is type in Go
	fmt.Println(x())				// Executing returned function

	fmt.Println(bar()())				// Cleaned up code
}

func foo() string {
	return "Hello Shital"
}

func bar() func() int {
	return func() int {
		return 451
	}
}

