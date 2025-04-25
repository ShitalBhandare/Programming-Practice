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

============================

OUTPUT:

2		10
4		100
1024			10000000000
1048576			100000000000000000000
1073741824		1000000000000000000000000000000
1024			10000000000
1048576			100000000000000000000
1073741824		1000000000000000000000000000000

Program exited.
