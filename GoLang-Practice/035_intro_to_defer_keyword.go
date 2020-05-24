package main

import (
	"fmt"
)

func main() {

	// defer keyword defers the execution of function till the program exits
	// It executes the defered functions in reverse order

	defer foo()
	defer bar()
	mouse()

	// prints 3 2 1 0 before surrounding function returns
	for i := 0; i <= 3; i++ {
		defer fmt.Println(i)
	}
}

func foo() {
	fmt.Println("In function foo")
}

func bar() {
	fmt.Println("In function bar")
}

func mouse() {
	fmt.Println("In function mouse")
}

