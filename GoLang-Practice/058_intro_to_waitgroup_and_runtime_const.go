package main

import (
	"fmt"
	"runtime"
	"sync"
)

var wg sync.WaitGroup

func main() {

	fmt.Println("OS\t\t:", runtime.GOOS)
	fmt.Println("ARCH\t\t:", runtime.GOARCH)
	fmt.Println("CPU\t\t:", runtime.NumCPU())
	fmt.Println("GORoutine\t:", runtime.NumGoroutine())

	/*Creating new GO routine by adding go at the beginning
	main_routine
	|
	|
	|\new_routine
	| \
	|  \

	After adding new routine, program does not wait for new routine to finish
	*/

	// Add 1 routine in waitgroup
	wg.Add(1)
	go foo()

	bar()

	// Wait until added go routine finishes
	wg.Wait()
}

func foo() {
	for i := 0; i < 5; i++ {
		fmt.Println("foo", i)
	}

	// Notify newly added routine is finished
	wg.Done()
}

func bar() {
	for i := 0; i < 5; i++ {
		fmt.Println("bar", i)
	}
}

