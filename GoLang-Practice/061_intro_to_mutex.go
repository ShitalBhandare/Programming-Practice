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

	var mu sync.Mutex

	for i := 0; i < gs; i++ {
		go func() {

			// Usage of mutex lock and unlock to avoid the race condition
			mu.Lock()
			runtime.Gosched()
			v := counter
			v++
			counter = v
			mu.Unlock()
			wg.Done()
		}()
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

======================OUTPUT==================

================OUTPUT================

No. of CPU: 8
No. of GORoutine: 1
No. of GORoutine: 2
No. of GORoutine: 2
No. of GORoutine: 3
No. of GORoutine: 2
No. of GORoutine: 3
No. of GORoutine: 3
No. of GORoutine: 2
No. of GORoutine: 3
No. of GORoutine: 3
No. of GORoutine: 3
No. of GORoutine: 3
No. of GORoutine: 2
No. of GORoutine: 3
No. of GORoutine: 2
No. of GORoutine: 3
No. of GORoutine: 3
No. of GORoutine: 2
No. of GORoutine: 3
No. of GORoutine: 4
No. of GORoutine: 5
No. of GORoutine: 6
No. of GORoutine: 7
No. of GORoutine: 8
No. of GORoutine: 9
No. of GORoutine: 10
No. of GORoutine: 11
No. of GORoutine: 12
No. of GORoutine: 13
No. of GORoutine: 14
No. of GORoutine: 15
No. of GORoutine: 16
No. of GORoutine: 3
No. of GORoutine: 4
No. of GORoutine: 3
No. of GORoutine: 3
No. of GORoutine: 3
No. of GORoutine: 3
No. of GORoutine: 2
No. of GORoutine: 3
No. of GORoutine: 4
No. of GORoutine: 5
No. of GORoutine: 6
No. of GORoutine: 2
No. of GORoutine: 2
No. of GORoutine: 3
No. of GORoutine: 2
No. of GORoutine: 2
No. of GORoutine: 2
No. of GORoutine: 3
No. of GORoutine: 3
No. of GORoutine: 3
No. of GORoutine: 2
No. of GORoutine: 3
No. of GORoutine: 2
No. of GORoutine: 2
No. of GORoutine: 3
No. of GORoutine: 2
No. of GORoutine: 2
No. of GORoutine: 3
No. of GORoutine: 3
No. of GORoutine: 2
No. of GORoutine: 3
No. of GORoutine: 3
No. of GORoutine: 2
No. of GORoutine: 3
No. of GORoutine: 4
No. of GORoutine: 5
No. of GORoutine: 2
No. of GORoutine: 2
No. of GORoutine: 3
No. of GORoutine: 2
No. of GORoutine: 3
No. of GORoutine: 4
No. of GORoutine: 2
No. of GORoutine: 3
No. of GORoutine: 3
No. of GORoutine: 3
No. of GORoutine: 2
No. of GORoutine: 3
No. of GORoutine: 3
No. of GORoutine: 3
No. of GORoutine: 2
No. of GORoutine: 3
No. of GORoutine: 3
No. of GORoutine: 2
No. of GORoutine: 2
No. of GORoutine: 2
No. of GORoutine: 3
No. of GORoutine: 3
No. of GORoutine: 2
No. of GORoutine: 2
No. of GORoutine: 3
No. of GORoutine: 3
No. of GORoutine: 3
No. of GORoutine: 3
No. of GORoutine: 2
No. of GORoutine: 3
No. of GORoutine: 3
No. of GORoutine: 2
No. of GORoutine: 3
No. of GORoutine: 3
Counter: 100

Program exited.

