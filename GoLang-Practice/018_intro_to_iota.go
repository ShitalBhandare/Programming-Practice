package main

import "fmt"


// iota => predeclared identifier => Successive untyped integer constant
// Starts with integer value 0 and increments value by 1 for next identifiers

const (
	a = iota
	b = iota
	c = iota
)

const (
	p = iota
	q
	r
)

func main () {
	fmt.Println(a, b, c)
	fmt.Printf("%T\t, %T\t, %T\n", a, b, c)
	fmt.Println(p, q, r)
}
