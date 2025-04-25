package main

import (
	"fmt"
)

const (
	year1 = 2020 + iota	// 2020
	year2 = 2020 + iota	// 2021
	year3 = 2020 + iota	// 2022
	year4 = 2020 + iota	// 2023

)

func main() {

	x := 100
	fmt.Printf("Decimal\t:%d\nBinary\t:%b\nHex\t:%#X\n",x, x, x)
	y := x << 1
	fmt.Printf("Decimal\t:%d\nBinary\t:%b\nHex\t:%#X\n",y, y, y)

	str1 := `shital,
	you are doing
	"awesome"`
	fmt.Println(str1)

	fmt.Println(year1, year2, year3, year4)
}

=========OUTPUT============


Decimal	:100
Binary	:1100100
Hex	:0X64
Decimal	:200
Binary	:11001000
Hex	:0XC8
shital,
	you are doing
	"awesome"
2020 2021 2022 2023
