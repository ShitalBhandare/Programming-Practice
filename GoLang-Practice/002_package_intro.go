package main

import "fmt"

func main() {
	// n := number of bytes returned
	// err := Any error thrown
	n, err := fmt.Println("Introduction to fmt package")
	fmt.Println(n, err)

	// Never write variable without use.
	// In this case go build will fail if err is not used.
	// fmt.Println(n)
}
