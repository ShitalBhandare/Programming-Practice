package main

import (
	"fmt"
)

func main() {

	// Normal function
	foo()

	// Anonymous func
	func () {
		fmt.Println("This is anonymous func")
	}()

	// Anonymous func with parameters
	func (x int) {
		fmt.Println("Anonymous func with parameters", x)
	} (42)

	// func expression: Assigning a func to variable
	f := func() {
		fmt.Println("My first func expression")
	}
	f()

	// func expression with parameters
	g := func(x int) {
		fmt.Println("The year when I born", x)
	}
	g(1995)
}

func foo() {
	fmt.Println("In func foo")
}
