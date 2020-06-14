package main

import (
	"fmt"
)

var copy func() int

func main() {

	// Exercise 6
	func() {
		fmt.Println("This is anonymous func")
	}()

	// Exercise 7
	a := foobar()
	fmt.Println(a)

	// Exercise 8
	x := demo_func()
	fmt.Printf("%T\n", x)
	fmt.Println(x())

	copy = demo_func()
	fmt.Printf("%T\n", copy)
	fmt.Println(copy())

	// Exercise 9
	callback_func(check)

	// Exercise 10
	f := new_func()
	fmt.Println(f())
	fmt.Println(f())
	g := new_func()
	fmt.Println(g())
	fmt.Println(g())
	fmt.Println(g())
}

func foobar() int {
	return 1995
}

func demo_func() func() int {
	return func() int {
		return 42
	}
}

func check() int {
	//fmt.Println("In check method")
	return 19
}

func callback_func(check func() int){
	ret := check()
	fmt.Println(ret)
}

func new_func() func() int {
	x := 5
	return func() int {
		x++
		return x
	}
}
