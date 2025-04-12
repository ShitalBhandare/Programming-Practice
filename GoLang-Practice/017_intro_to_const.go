package main

import (
	"fmt"
)

// Untyped constant
const w = 2.78
const x = 12
const y = true
const z = "shital"

// Typed constant
const a int = 1
const b string = "bhandare"
const c bool = false
const d float64 = 2.3

// Combining const values
const (
	p int = 3
	q bool = true
)

func main() {
	fmt.Println(w)
	fmt.Println(x)
	fmt.Println(y)
	fmt.Println(z)
	fmt.Printf("%T\n", w)
	fmt.Printf("%T\n", x)
	fmt.Printf("%T\n", y)
	fmt.Printf("%T\n", z)

	fmt.Println(a)
	fmt.Println(b)
	fmt.Println(c)
	fmt.Println(d)
	fmt.Printf("%T\n", a)
	fmt.Printf("%T\n", b)
	fmt.Printf("%T\n", c)
	fmt.Printf("%T\n", d)

	fmt.Println(p, q)
}

====================OUTPUT===================

2.78
12
true
shital
float64
int
bool
string
1
bhandare
false
2.3
int
string
bool
float64
3 true
