package main

import (
	"fmt"
)

func main() {

	c := make(chan int)

	// send 
	go foo(c)

	// receive
	//go bar(c)			// these go routines will never send/receive at the same time
	bar(c)

	fmt.Println("About to exit")
}

// send
func foo(c chan <- int){
	c <- 19
}

// receive
func bar(c <- chan int){
	fmt.Println(<-c)
}


=============OUTPUT==========

19
About to exit

Program exited.
