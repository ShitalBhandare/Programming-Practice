package main

import (
	"fmt"
	"runtime"
)

var a int = 12
var b float64 = 15

func main() {

	x := 42.1211
	y := 20
	fmt.Println("x:",x)
	fmt.Println("y:",y)

	fmt.Printf("%T\n",x)
	fmt.Printf("%T\n",y)

	x = 175  // This will work
	fmt.Println("x:",x)

	// y = 35.13 This will not work

	fmt.Println("a:",a)
	fmt.Println("b:",b)

	fmt.Println("GOOS:",runtime.GOOS)
	fmt.Println("GOARCH:",runtime.GOARCH)
}

===============OUTPUT===========================

x: 42.1211
y: 20
float64
int
x: 175
a: 12
b: 15
GOOS: linux
GOARCH: amd64
