package main

import (
	"fmt"
)

func main() {
	var s = "S"
	fmt.Println(s)
	fmt.Printf("%s\n", s)

	bs := []byte(s)
	n := bs[0]

	fmt.Printf("Decimal:%d\n", n)
	fmt.Printf("Hex:%x\n", n)
	fmt.Printf("Binary:%b\n", n)
	fmt.Printf("Octal:%o\n", n)

	// %#x => Prepends 0x
	fmt.Printf("HexaDecimal:%#x\n", n)
}

=================OUTPUT=====================


S
S
Decimal:83
Hex:53
Binary:1010011
Octal:123
HexaDecimal:0x53
