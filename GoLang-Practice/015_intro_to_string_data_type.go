package main

import (
	"fmt"
)

func main() {

	// Use of double quotes
	var str1 string = "Shital Bhandare"

	// Raw string using backticks
	str2 := `You Are Doing "much"
	Great`

	// String Printing
	fmt.Println("str1:", str1)
	fmt.Printf("%T\n", str1)
	fmt.Println("str2:", str2)
	fmt.Printf("%T\n", str2)


	// String formatting
	fmt.Printf("%s\n", str1)
	fmt.Printf("%q\n", str1)
	fmt.Printf("%x\n", str2)

	// String reassignment
	str2 = "Hey"
	fmt.Println("str2:", str2)

	// String as a Sequence of Bytes
	bs := []byte(str1)
	fmt.Println("bs:", bs)

	// String iteration
	for i := 0; i < len(str1); i++ {
		fmt.Printf("%x ", str1[i])
	}
	fmt.Println()

	// String iteration
        for i := 0; i < len(str1); i++ {
                fmt.Printf("%d ", str1[i])
        }
	fmt.Println()

	// String iteration
	for i, v := range(str1) {
                fmt.Printf("At index position %d, we have value %#U \n", i, v)
        }

}

