package main

import "fmt"


// DECLARE a VARIABLE with IDENTIFIER "z"
// and ASSIGN a VALUE 21
var z int = 21


// DECLARE a VARIABLE with IDENTIFIER "str"
// and ASSIGN a VALUE "Shital"
var str string = "Shital"


// GoLang is a STATIC programming language.
// A VARIABLE is assigned to hold a value of specific type only.
// Not a DYNAMIC programming language

func main() {

	fmt.Println("z:", z)
	fmt.Printf("%T\n", z)

	fmt.Println("str:", str)
        fmt.Printf("%T\n", str)

	// Below will raise a eror
	// z = "Bhandare"

	// Use of backticks `` for printing raw string
	new_str := `You are doing "GREAT"`
	fmt.Println("new_str:", new_str)

	// Use of backticks for printing multiple lines
	multiline_str := `This is me, Shital,
	Learning GoLang
	AND
	Enjoying a lot`
	fmt.Println("multiline_str:", multiline_str)

}
