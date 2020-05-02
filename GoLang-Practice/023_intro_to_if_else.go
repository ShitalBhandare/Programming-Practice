package main

import (
	"fmt"
)

func main() {

	// Scope limited to if statement
	if x := 42; x == 42 {
		fmt.Println("Its equal")
	}

	if true {
		fmt.Println("Its true")
	}

	if false {
		fmt.Println("Control will not come here as its false")
	}

	x := 43
	if x == 42 {
		fmt.Println("Our value is 42")
	} else if x == 43 {
		fmt.Println("Our value is 43")
	} else {
		fmt.Println("Our value is neither 42 nnor 43")
	}
}

