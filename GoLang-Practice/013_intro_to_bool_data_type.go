package main

import "fmt"

var x bool

func main() {
	fmt.Println("X:", x)
	x = true
	fmt.Println("After assignment X:", x)
	a := 10
	b := 20
	fmt.Println(a == b)

}


=================Output===================


X: false
After assignment X: true
false

Program exited.
