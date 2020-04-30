package main

import (
	"fmt"
)

func main() {

	// for initial; condition; post
	for i := 0; i < 5; i++ {
		fmt.Println(i)
	}

	// Nested Loop
	for i := 0; i < 5; i++ {
		fmt.Printf("The outer loop: %d\n", i)
		for j := 0; j < 3; j++ {
			fmt.Printf("\t\tThe innerr loop: %d\n", j)
		}
	}

	// Like C (;;) Usage of break and continue
	i := 1
	for {
		i++
		if i > 20 {
			break
		}
		if i % 2 == 1 {
			continue
		}
		fmt.Println(i)

	}

	// Similar to while loop
	j := 1
        for j < 15 {
		j = j*2
                fmt.Println(j)
        }

	// Printing ASCII values
	for i := 33; i < 122; i++ {
		fmt.Printf("%v\t\t%#U\n", i, i)
	}
}

