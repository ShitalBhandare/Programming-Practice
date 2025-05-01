package main

import (
	"fmt"
	"math"
)

type person struct {
	first string
	last  string
	age   int
}

type square struct {
	length float64
}

type circle struct {
	radius float64
}

type shape interface {
	area() float64
}

func main() {

	// Exercise 1
	fmt.Println(foo())
	fmt.Println(bar())

	// Exercise 2
	s1 := []int{1, 2, 3, 4, 5, 6, 7, 8, 9}

	// Passing int values.. i.e. unfurling the slice
	fmt.Println(foo1(s1...))

	// Passing slice of int
	fmt.Println(bar1(s1))

	// Exercise 3
	defer func_to_defer()
	demo()
	test()

	// Exercise 4
	p1 := person{
		first: "James",
		last:  "Bond",
		age:   32,
	}

	p1.speak()

	// Exercise 5
	s2 := square{
		length: 10.76,
	}

	c1 := circle{
		radius: 5.082,
	}
	fmt.Println(s2)
	fmt.Println(c1)
	info(s2)
	info(c1)
}

func foo() int {
	return 19
}

func bar() (int, string) {
	return 1873, "Shital"
}

func foo1(xi ...int) int {
	total := 0
	for _, v := range xi {
		total += v
	}
	return total
}

func bar1(xi []int)  int{
	total := 0
	for _, v := range xi {
		total += v
	}
	return total
}

func func_to_defer() {
	fmt.Println("Func to defer")
}

func demo() {
	fmt.Println("Demo func")
}

func test() {
	fmt.Println("test func")
}

func (p person) speak() {
	fmt.Println("I am", p.first, p.last, "and I am", p.age, "years old.")
}

func (c circle) area() float64 {
	return math.Pi * c.radius * c.radius
}

func (s square) area() float64 {
	return s.length * s.length
}

func info(s shape) {
	fmt.Println(s.area())
}


===========OUTPUT==========

19
1873 Shital
45
45
Demo func
test func
I am James Bond and I am 32 years old.
{10.76}
{5.082}
115.77759999999999
81.13704638469119
Func to defer
