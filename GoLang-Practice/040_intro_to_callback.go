package main

import (
	"fmt"
)

func main() {

	slice := []int{1, 2, 3, 4, 5, 6, 7, 8, 9}

	s1 := sum(slice...)
	fmt.Println("Total Sum:", s1)

	// Callback is passing a func as an argument to other func
	s2 := evenSum(sum, slice...)
	fmt.Println("Even Sum:", s2)

	s3 := oddSum(sum, slice...)
	fmt.Println("Odd Sum:", s3)
}

func sum(y ...int) int {
	total := 0
	for _, v := range y {
		total += v
	}
	return total
}

func evenSum(f func(l ...int) int, j ...int) int {
	var xi []int
	for _, v := range j {
		if v % 2 == 0 {
			xi = append(xi, v)
		}
	}

	return f(xi...)
}

func oddSum(f func(l ...int) int, j ...int) int {
	var xi []int
	for _, v := range j {
		if v % 2 != 0 {
			xi = append(xi, v)
		}
	}

	return f(xi...)
}


==============OUTPUT===========

Total Sum: 45
Even Sum: 20
Odd Sum: 25

