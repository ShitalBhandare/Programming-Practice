package main

import (
	"fmt"
)

func main() {

	eve := make(chan int)
	odd := make(chan int)
	quit := make(chan int)

	// send
	go send(eve, odd, quit)

	// receive
	receive(eve, odd, quit)

	fmt.Println("About to exit")
}

func send(eve, odd, quit chan<- int) {
	for i := 0; i < 20; i++ {
		if i%2 == 0 {
			eve <- i
		} else {
			odd <- i
		}
	}
	quit <- 0
}

func receive(eve, odd, quit <-chan int) {
	for {
		select {
		case v := <-eve:
			fmt.Println("From eve channel:", v)
		case v := <-odd:
			fmt.Println("From odd channel:", v)
		case v := <-quit:
			fmt.Println("From quit channel:", v)
			return
		}
	}
}

