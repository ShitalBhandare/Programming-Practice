package main

import (
	"fmt"
	"sync"
)

var wg sync.WaitGroup

func main() {

	fmt.Println("Program for usage of goroutine")

	wg.Add(2)
	go func1()
	go func2()
	wg.Wait()
}

func func1(){
	fmt.Println("In Go Routine 1")
	wg.Done()
}

func func2(){
	fmt.Println("In Go Routine 2")
	wg.Done()
}

