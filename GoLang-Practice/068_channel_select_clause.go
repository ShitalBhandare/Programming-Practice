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

=====================OUTPUT================


From eve channel: 0
From odd channel: 1
From eve channel: 2
From odd channel: 3
From eve channel: 4
From odd channel: 5
From eve channel: 6
From odd channel: 7
From eve channel: 8
From odd channel: 9
From eve channel: 10
From odd channel: 11
From eve channel: 12
From odd channel: 13
From eve channel: 14
From odd channel: 15
From eve channel: 16
From odd channel: 17
From eve channel: 18
From odd channel: 19
From quit channel: 0
About to exit

Program exited.

