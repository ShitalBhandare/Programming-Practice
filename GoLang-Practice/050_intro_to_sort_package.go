package main

import (
	"fmt"
	"sort"			// Package for Sorting
)

func main() {

	si := []int{2, 1, 6, 4, 8, 5, 9}
	fmt.Println(si)
	sort.Ints(si)
	fmt.Println(si)

	fmt.Println("--------")

	ss := []string{"Shital", "Bhandare", "Priya", "James", "Bond"}
	fmt.Println(ss)
	sort.Strings(ss)
	fmt.Println(ss)
}


==============OUTPUT============

[2 1 6 4 8 5 9]
[1 2 4 5 6 8 9]
--------
[Shital Bhandare Priya James Bond]
[Bhandare Bond James Priya Shital]

Program exited.
