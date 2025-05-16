package main

import (
	"fmt"
)

func main() {

	c := make(chan int)
	fmt.Printf("Type of chan c: %T", c)

	// Directional Channel: can only send/receive
	cs := make(chan <- int)
	fmt.Printf("\nType of chan cs: %T", cs)

	cr := make(<- chan int)
	fmt.Printf("\nType of chan cr: %T", cr)

	//cs <- 42
	//fmt.Println(<-cs)  				Error: <-cs (receive from send-only type chan<- int)

	//cr <- 43					Error: cr <- 43 (send to receive-only type <-chan int)	

	/*
	//Assignment: specific to generic and specific to specific will not work 
	c = cr
	fmt.Printf("Type of chan c: %T", c)
	c = cs
	fmt.Printf("Type of chan c: %T", c)
	cr = cs
	fmt.Printf("Type of chan c: %T", cr)
	*/

	//Assignment: generic to specific will work
	fmt.Println("-----")
	cr = c
	fmt.Printf("\nType of chan cr: %T", cr)
	cs = c
	fmt.Printf("\nType of chan cs: %T", cs)

	// Conversion: generic to specific will work
	fmt.Println("-----")
	fmt.Printf("c\t%T\n", (<-chan int)(c))
	fmt.Printf("c\t%T\n", (chan<- int)(c))

	/*
	// Conversion: specific to generic will not work
	fmt.Println("-----")
	fmt.Printf("cr\t%T\n", (chan int)(cr))
	fmt.Printf("cs\t%T\n", (chan int)(cs))
	*/
}

=================OUTPUT=========

Type of chan c: chan int
Type of chan cs: chan<- int
Type of chan cr: <-chan int-----

Type of chan cr: <-chan int
Type of chan cs: chan<- int-----
c	<-chan int
c	chan<- int

Program exited.

