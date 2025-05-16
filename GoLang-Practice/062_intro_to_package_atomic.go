package main

import (
	"fmt"
	"runtime"
	"sync"
	"sync/atomic"
)

func main() {

	// Creating race condition

	fmt.Println("No. of CPU:", runtime.NumCPU())
	fmt.Println("No. of GORoutine:", runtime.NumGoroutine())

	var counter int64
	const gs = 100
	var wg sync.WaitGroup
	wg.Add(gs)

	for i := 0; i < gs; i++ {
		go func() {
			atomic.AddInt64(&counter, 1)
			runtime.Gosched()
			atomic.LoadInt64(&counter)
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

===========OUTPUT=========

No. of CPU: 8
No. of GORoutine: 1
No. of GORoutine: 2
No. of GORoutine: 3
No. of GORoutine: 4
No. of GORoutine: 5
No. of GORoutine: 2
No. of GORoutine: 3
No. of GORoutine: 2
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
No. of GORoutine: 17
No. of GORoutine: 18
No. of GORoutine: 19
No. of GORoutine: 20
No. of GORoutine: 21
No. of GORoutine: 22
No. of GORoutine: 23
No. of GORoutine: 24
No. of GORoutine: 25
No. of GORoutine: 26
No. of GORoutine: 27
No. of GORoutine: 28
No. of GORoutine: 29
No. of GORoutine: 30
No. of GORoutine: 31
No. of GORoutine: 32
No. of GORoutine: 33
No. of GORoutine: 34
No. of GORoutine: 35
No. of GORoutine: 36
No. of GORoutine: 37
No. of GORoutine: 38
No. of GORoutine: 39
No. of GORoutine: 40
No. of GORoutine: 41
No. of GORoutine: 42
No. of GORoutine: 43
No. of GORoutine: 44
No. of GORoutine: 45
No. of GORoutine: 46
No. of GORoutine: 47
No. of GORoutine: 48
No. of GORoutine: 49
No. of GORoutine: 50
No. of GORoutine: 51
No. of GORoutine: 52
No. of GORoutine: 2
No. of GORoutine: 3
No. of GORoutine: 4
No. of GORoutine: 2
No. of GORoutine: 3
No. of GORoutine: 4
No. of GORoutine: 5
No. of GORoutine: 6
No. of GORoutine: 7
No. of GORoutine: 8
No. of GORoutine: 9
No. of GORoutine: 3
No. of GORoutine: 3
No. of GORoutine: 2
No. of GORoutine: 3
No. of GORoutine: 2
No. of GORoutine: 3
No. of GORoutine: 3
No. of GORoutine: 2
No. of GORoutine: 3
No. of GORoutine: 2
No. of GORoutine: 3
No. of GORoutine: 2
No. of GORoutine: 3
No. of GORoutine: 2
No. of GORoutine: 3
No. of GORoutine: 2
No. of GORoutine: 3
No. of GORoutine: 2
No. of GORoutine: 3
No. of GORoutine: 3
No. of GORoutine: 2
No. of GORoutine: 3
No. of GORoutine: 2
No. of GORoutine: 3
No. of GORoutine: 4
No. of GORoutine: 5
No. of GORoutine: 6
No. of GORoutine: 7
No. of GORoutine: 8
No. of GORoutine: 9
No. of GORoutine: 1
Counter: 100

Program exited.

