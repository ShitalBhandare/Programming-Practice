package main

import (
	"fmt"
)

func main() {

	// Array in Go is not same as array in C.
	// when array is passed to function, it copies all elements of array.
	// Use slice instead of array in Go.
	// len is type of array. hence [10]int and [20]int are 2 different arrays.

	// Array declaration
	var array [5] int
	fmt.Println("Array:", array)

	array[0] = 1
	fmt.Println("Array after modification:", array)

	// Built-in function to find length of array
	fmt.Println("Length of array:", len(array))
}

==============OUTPUT============


Array: [0 0 0 0 0]
Array after modification: [1 0 0 0 0]
Length of array: 5

Program exited.

