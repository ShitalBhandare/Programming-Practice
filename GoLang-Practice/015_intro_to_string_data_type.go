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


=====================OUTPUT=====================


str1: Shital Bhandare
string
str2: You Are Doing "much"
	Great
string
Shital Bhandare
"Shital Bhandare"
596f752041726520446f696e6720226d756368220a094772656174
str2: Hey
bs: [83 104 105 116 97 108 32 66 104 97 110 100 97 114 101]
53 68 69 74 61 6c 20 42 68 61 6e 64 61 72 65 
83 104 105 116 97 108 32 66 104 97 110 100 97 114 101 
At index position 0, we have value U+0053 'S' 
At index position 1, we have value U+0068 'h' 
At index position 2, we have value U+0069 'i' 
At index position 3, we have value U+0074 't' 
At index position 4, we have value U+0061 'a' 
At index position 5, we have value U+006C 'l' 
At index position 6, we have value U+0020 ' ' 
At index position 7, we have value U+0042 'B' 
At index position 8, we have value U+0068 'h' 
At index position 9, we have value U+0061 'a' 
At index position 10, we have value U+006E 'n' 
At index position 11, we have value U+0064 'd' 
At index position 12, we have value U+0061 'a' 
At index position 13, we have value U+0072 'r' 
At index position 14, we have value U+0065 'e' 

Program exited.

