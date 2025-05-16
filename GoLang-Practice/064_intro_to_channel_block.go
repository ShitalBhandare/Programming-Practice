package main

import (
	"fmt"
)

func main() {


	c := make(chan int)

	/* Below code does not run because channel blocks.
	Channels are synchronous. They have to send/receive values at the same time.
	c <- 19
	fmt.Println(<-c)
	*/

	// This will work as channel has sent some value in another go routine.
	// This new go routine will block and not the main one.
	go func() {
		c <- 19
	}()
	fmt.Println(<-c)


	// Below code will work.
	// Buffered channel => allows to keep some value in channel as a buffer

	ch := make(chan int, 1)  // can keep 1 value as a buffer
	ch <- 20
	fmt.Println(<-ch)

	/*
	// Below code will not work.
	dh := make(chan int, 1)  // can keep 1 value as a buffer
	dh <- 20
	dh <- 21		// passing 2 values to channel, so it will blcok
	fmt.Println(<-dh)
	*/

	// Below code will work.
	kh := make(chan int, 2)  // can keep 1 value as a buffer
	kh <- 21
	kh <- 22
	fmt.Println(<-kh)
	fmt.Println(<-kh)

}

================OUTPUT===========

19
20
21
22

Program exited.

