package main

import (
	"fmt"
)

func main() {

	c := make(chan int)

	go func(){
		for i:= 0; i<10; i++{
			c <- i
		}
		close(c)
	}()

	// range reads over a channel until a channel is closed
	for v := range c{
		fmt.Println(v)
	}

	fmt.Println("Done")
}

=================OUTPUT=============

0
1
2
3
4
5
6
7
8
9
Done

Program exited.
