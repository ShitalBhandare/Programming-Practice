package main

import (
	"fmt"
)

func doSomething(i int) int {
	return i*5
}

func main() {

	ch := make(chan int)

	// New go routine throws out the value returned.
	// Hence, wrap around the value in channel
	go func() {
		ch <- doSomething(3)
	}()
	fmt.Println(<-ch)
}

==============OUTPUT=============

15
