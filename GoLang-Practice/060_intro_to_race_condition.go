package main

import (
	"fmt"
	"runtime"
	"sync"
)

func main() {

	// Creating race condition

	fmt.Println("No. of CPU:", runtime.NumCPU())
	fmt.Println("No. of GORoutine:", runtime.NumGoroutine())

	counter := 0
	const gs = 100
	var wg sync.WaitGroup
	wg.Add(gs)

	for i := 0; i < gs; i++ {
		go func() {
			runtime.Gosched()
			v := counter
			v++
			counter = v

		}()
		wg.Done()
		fmt.Println("No. of GORoutine:", runtime.NumGoroutine())
	}
	wg.Wait()
	fmt.Println("No. of GORoutine:", runtime.NumGoroutine())

	fmt.Println("Counter:", counter)

	/*
	To find the data race:
	go run --race 060_intro_to_race_condition.go
	output:
	Counter: 100
	Found 1 data race(s)
	exit status 66
	*/

}

