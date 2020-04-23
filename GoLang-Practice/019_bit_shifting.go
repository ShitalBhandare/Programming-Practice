package main

import (
	"fmt"
)

const (
	_ = iota 			// 0
	KB = 1 << (iota * 10)		// 1 << (1 * 10)
	MB = 1 << (iota * 10)		// 2 << (2 * 10)
	GB = 1 << (iota * 10)		// 3 << (3 * 10)
)
func main() {

	x := 2
	fmt.Printf("%d\t\t%b\n", x, x)

	// Bit Shifting
	y := x << 1
	fmt.Printf("%d\t\t%b\n", y, y)

	kb := 1024
	mb := 1024 * kb
	gb := 1024 * mb

	fmt.Printf("%d\t\t\t%b\n", kb, kb)
	fmt.Printf("%d\t\t\t%b\n", mb, mb)
	fmt.Printf("%d\t\t%b\n", gb, gb)

	fmt.Printf("%d\t\t\t%b\n", KB, KB)
	fmt.Printf("%d\t\t\t%b\n", MB, MB)
	fmt.Printf("%d\t\t%b\n", GB, GB)

}

