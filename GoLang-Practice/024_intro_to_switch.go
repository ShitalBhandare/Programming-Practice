package main

import (
	"fmt"
)

func main() {

	// Switch behavior: 2 types - Expression and Type
	// 1. Expression switch => Switches case based on expression

	switch {
	case false:
		fmt.Println("This should not print")
	case (2 == 2):
		fmt.Println("This should print")
		fallthrough
	case (4 == 4): // Without fallthrough, this code will not execute.
		fmt.Println("With fallthrough, this will print")
		fallthrough
	// Funky fallthrough
	case (1 == 2):
		fmt.Println("Becasue of fallthrough, this will also print")
		fallthrough
	case (5 == 5):
		fmt.Println("prints")
	//Defalut case
	default:
		fmt.Println("This is the default case.")
	}

	// Switching on variable and using multiple values to it
	x := "Shital"
	switch x {
	case "shital", "Shital", "Sheetal":
		fmt.Println("Its me, Shital")
	case "bhandare":
		fmt.Println("Its my surname, Bhandare")
	default:
		fmt.Println("Nothing")
	}

	/* 2. Type Switch :=> x should be type of interface{}
	switch x.(type){
	case string:
		fmt.println("String data type")
	case int:
		fmt.Println("Integer data type")
	}
	*/

	// Conditional operator
	fmt.Println(true && true)
	fmt.Println(true && false)
	fmt.Println(true || true)
	fmt.Println(true || false)
	fmt.Println(!true)


}

==============OUTPUT============

This should print
With fallthrough, this will print
Becasue of fallthrough, this will also print
prints
Its me, Shital
true
false
true
true
false

Program exited.

