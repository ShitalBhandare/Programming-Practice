package main

import (
	"fmt"
)

func main() {

	c := make(chan int)
	go func(){
		c <- 19
		close(c)
	}()

	v, ok := <- c
	fmt.Println(v, ok)

	v, ok = <- c
	fmt.Println(v, ok)

}

=============OUTPUT============

19 true
0 false

Program exited.
