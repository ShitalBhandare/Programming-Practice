package main

import (
	"fmt"
	"math"
)

// Intro to Method sets in GO

type circle struct {
	radius float64
}

func (c circle) area() float64 {
	return math.Pi * c.radius * c.radius
}

type shape interface {
	area() float64
}

func info(s shape) {
	fmt.Println(s.area())
}

func main() {

	c := circle{
		radius: 5,
	}

	// Receiver: Non-Pointer and value: Non-Pointer
	info(c)

	// Receiver: Non-Pointer and Value: Pointer		
	info(&c)

	/*
	Receiver: Pointer and Value: Pointer
	value:	info(&c)
	Receiver:	func (c *circle) area() float64  
	
	Receiver: Pointer and Value: Non Pointer			=> This will not work
	value:	info(c)
	Receiver:	func (c *circle) area() float64  
	
	
	Receivers       Values
	-----------------------------------------------
	(t T)           T and *T
	(t *T)          *T
	*/

}

