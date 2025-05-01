package main

import (
	"fmt"
)

func main() {

	// Intro to functions
	// func (r receiver) identifier(parameters) (return(s)) { ... }

	foo()
	bar("shital")
	ret := woo("bhandare")
	fmt.Println(ret)
	x, y := mouse("Miss", "Moneypenny")
	fmt.Println(x)
	fmt.Println(y)
}

// Basic function
func foo() {
	fmt.Println("Hello from foo")
}

// Functions with parameters
func bar(s string) {							// scope of s is upto function only
	fmt.Println("Hello, ", s)
}

// Functions with returns
func woo(ln string) string {
	return fmt.Sprint("Hey, ", ln)
}

// Functions with multiple returns
func mouse(fn string, ln string) (string, bool) {
	a := fmt.Sprint(fn, " ", ln)
	return a, true
}


===============OUTPUT===========

Hello from foo
Hello,  shital
Hey, bhandare
Miss Moneypenny
true
