package main

import (
	"fmt"
)

type customErr struct {
	info string
}

func (ce customErr) Error() string {
	return fmt.Sprintf("Here is the error info: %v ", ce.info)
}

func main() {

	c1 := customErr{
		info: "Need this lockdown to get ended quickly",
	}

	foo(c1)
}

func foo(e error) {
	fmt.Println(e)
	// fmt.Println(e.info) => will not work as type error has no field or method info
	// Need to do assertion
	fmt.Println(e.(customErr).info)
}

