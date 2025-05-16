package main

import (
	"errors"
	"fmt"
)

func main() {

	// Errors with more info

	v, err := sqrt(-10)
	fmt.Println(v, err)

	v, err = cuberrot(-5)
	fmt.Println(v, err)
}

func sqrt(f float64) (float64, error) {
	fmt.Println("In sqrt func")
	if f < 0 {
		// Plain error string
		er := errors.New("Invalid value to get square root")
		return 0.0, er
	}
	return 41, nil
}

func cuberrot(f float64) (float64, error) {
	fmt.Println("In cuberoot func")
	if f < 0 {
		// Formatted error string
		er := fmt.Errorf("Invalid value %f to get cube root", f)
		return 0.0, er
	}
	return 42, nil
}

=============OUTPUT==========

In sqrt func
0 Invalid value to get square root
In cuberoot func
0 Invalid value -5.000000 to get cube root

Program exited.
