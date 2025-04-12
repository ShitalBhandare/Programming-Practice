package main

import "fmt"

var i int

// Create your own type
// my_type : type name and
// int : underlying type
type my_type int

func main() {
	i = 19
	fmt.Println("i:", i)
	fmt.Printf("Type of i: %T\n", i)

	var j my_type = 20
	fmt.Println("j:", j)
	fmt.Printf("Type of j: %T\n", j)

	// Cannot assign of something "my_type" to "int"
	// Even if my_type's underlying type is int
	// Both of them are completely different type
	//i = j

	// There is no CASTING in GO but it is CONVERSION
	i = int(j)
	fmt.Println("i:", i)
        fmt.Printf("Type of i: %T\n", i)

	i = 21
	j = my_type(i)
	fmt.Println("j:", j)
        fmt.Printf("Type of j: %T\n", j)
}

================OUTPUT=================

i: 19
Type of i: int
j: 20
Type of j: main.my_type
i: 20
Type of i: int
j: 21
Type of j: main.my_type
