package main

import (
	"fmt"
)

func main() {

	f := factorial(5)
	fmt.Println(f)

	f1 := fact_loop(6)
	fmt.Println(f1)
}

func factorial(n int) int {
	if n == 0 {
		return 1
	}
	return n * factorial(n-1)
}

func fact_loop(n int) int {
	total := 1
	for ; n > 0; n-- {
		total *= n
	}
	return total
}
