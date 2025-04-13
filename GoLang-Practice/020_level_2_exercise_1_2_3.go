package main

import (
	"fmt"
)

const (
	q = 87.76
	y string = "Shital"
)

func main() {
	number := 10
	fmt.Printf("Decimal: %d\nBinary: %b\nHex: %X\n", number, number, number)

	op1 := 20
	op2 := 30

	a := op1 == op2
	b := op1 <= op2
	c := op1 >= op2
	d := op1 != op2
	e := op1 < op2
	f := op1 > op2
	fmt.Println(a,b,c,d,e,f)

	fmt.Println(q, y)

}

===============OUTPUT==============

Decimal: 10
Binary: 1010
Hex: A
false true false true true false
87.76 Shital

Program exited.

