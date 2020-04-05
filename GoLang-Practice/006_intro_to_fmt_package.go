package main

import "fmt"

var i int = 123

var str string ="Shital"

func main() {

	// Various integer formats 
	fmt.Printf("Decimal value of i: %d\n", i)
	fmt.Printf("Binary value of i: %b\n", i)
	fmt.Printf("Octal value of i: %o\n", i)
	fmt.Printf("Hex value of i: %x\n", i)
	fmt.Printf("Hex value of i prependend with 0X: %#x\n", i)
	fmt.Printf("Deafult value of i: %v\n", i)
	fmt.Printf("Type of i: %T\n", i)
	fmt.Printf("Character representation of i: %c\n", i)
	fmt.Printf("Unicode format of i: %U\n", i)

	// Does not add a new line
	fmt.Print("i:", i, "\n")
	// Adds a new line
	fmt.Println("i:", i)
	// Needs format string and does not add new line
	fmt.Printf("i:%v", i)

	// Sprint or Sprintf or Sprintln.. similar to above
	// Its just that it prints to String which can assign to variable
	new_str := fmt.Sprint(str)
	fmt.Printf("\nnew_str: %s\n", new_str)

	// Fprint or Fprintf or Fprintn.. similar to above
	// Its just that it prints to file

}
