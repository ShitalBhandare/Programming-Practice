package main

import (
	"fmt"
)

func main() {

	s1 := []int{1, 2, 3, 4, 5}
	sum1 := sum(s1...)		// Unfurling a slice
	fmt.Println("The sum is", sum1)

	// sum1 := sum(s1)		// This will not work since function sum is expecting int values and not a slice of int

	sum1 = sum()			// It works since variadic parameters means ZERO or MORE values
	fmt.Println("The sum is", sum1)

	//sum1 = sum(s1..., "James")	// This will not work. Since VARIADIC Parameter should always be a FINAL parameter to function.
	//sum1 = sum("James", s1...)	// This will work.

}

func sum(x ...int) int {		// Function with variadic parameters.
	fmt.Println(x)
	fmt.Printf("%T\n", x)		// Slice of int

	sum := 0
	for _, v := range x {
		sum += v
	}
	return sum
}

=======================OUTPUT===================


[1 2 3 4 5]
[]int
The sum is 15
[]
[]int
The sum is 0
