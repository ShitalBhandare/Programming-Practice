package main

import (
	"fmt"
	//"log"
	"os"
)

func main() {
	_, err := os.Open("file.txt")
	fmt.Println("In main goroutine")
	defer foo()
	if err != nil {
		// Prints the err to standard out
		//fmt.Println(err)

		// Logs the error
		//log.Println(err)

		// Logs the errors and defers the func which were deferred.
		// Fatal is dead. Its ljust log the errors and call sys.exit(1)
		//log.Fatalln(err)

		// Logs the error and executes any deferred function
		//log.Panicln(err)

		panic(err)
	}
}

func foo() {
	fmt.Println("In func foo")
}

================OUTPUT=============

In main goroutine
In func foo
panic: open file.txt: no such file or directory

goroutine 1 [running]:
main.main()
	/tmp/sandbox233797445/prog.go:27 +0xaf

Program exited.
