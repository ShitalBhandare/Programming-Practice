package main

import (
	"fmt"
)


func main() {
	sum := sum(1, 2, 3, 4, 5)
	fmt.Println("The sum is", sum)

	lp := sum(10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
	fmt.Println("The sum is", lp)

}

func sum(x ...int) int {		// Function with variadic parameters
	fmt.Println(x)
	fmt.Printf("%T\n", x)		// Slice of int

	sum := 0
	for _, v := range x {
		sum += v
	}
	return sum
}

