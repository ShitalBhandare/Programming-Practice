package main

import (
	"fmt"
)

func main() {

	// Exercise 1
	array := [5]int{10, 20, 30, 40, 50}
	for i, v := range array {
		fmt.Println(i, v)
	}
	fmt.Printf("Type of array: %T\n", array)

	// Exercise 2
	slice := []int{42, 43, 44, 45, 46, 47, 48, 49, 50, 51}
	for i, v := range slice {
		fmt.Println(i, v)
	}
	fmt.Printf("Type of slice: %T\n", slice)

	// Exercise 3
	fmt.Println(slice[:5])
	fmt.Println(slice[5:])
	fmt.Println(slice[2:7])
	fmt.Println(slice[1:6])
	fmt.Println(slice)

	// Exercise 4
	x := []int{42, 43, 44, 45, 46, 47, 48, 49, 50, 51}
	x = append(x, 52)
	fmt.Println(x)
	x = append(x, 53, 54, 55)
	fmt.Println(x)

	y := []int{56, 57, 58, 59, 60}
	x = append(x, y...)
	fmt.Println(x)

	// Exercise 5 
	a := []int{42, 43, 44, 45, 46, 47, 48, 49, 50, 51}
	a = append(a[:2], a[6:]...)
	fmt.Println(a)

	// Exercise 6
	slice1 := make([]string, 50, 100)
	slice1 = []string{` Alabama`, ` Alaska`, ` Arizona`, ` Arkansas`, ` California`, ` Colorado`, ` Connecticut`, ` Delaware`, ` Florida`, ` Georgia`, ` Hawaii`, ` Idaho`, ` Illinois`, ` Indiana`, ` Iowa`, ` Kansas`, ` Kentucky`, ` Louisiana`, ` Maine`, ` Maryland`, ` Massachusetts`, ` Michigan`, ` Minnesota`, ` Mississippi`, ` Missouri`, ` Montana`, ` Nebraska`, ` Nevada`, ` New Hampshire`, ` New Jersey`, ` New Mexico`, ` New York`, ` North Carolina`, ` North Dakota`, ` Ohio`, ` Oklahoma`, ` Oregon`, ` Pennsylvania`, ` Rhode Island`, ` South Carolina`, ` South Dakota`, ` Tennessee`, ` Texas`, ` Utah`, ` Vermont`, ` Virginia`, ` Washington`, ` West Virginia`, ` Wisconsin`, ` Wyoming`}
	fmt.Println(slice1)
	fmt.Println(len(slice1))
	fmt.Println(cap(slice1))

	for i := 0; i < len(slice1); i++ {
		fmt.Println(i, slice1[i])
	}

	// Exercise 7

	s1 := []string{"James", "Bond", "Shaken, not stirred"}
	s2 := []string{"Miss", "Moneypenny", "Helloooooo, James."}

	s := [][]string{s1, s2}
	fmt.Println(s)

	for j := 0; j < len(s); j++ {
		fmt.Println(j, s[j])
		for k := 0; k < len(s[j]); k++ {
			fmt.Println(k, s[j][k])
		}
	}

	m := map[string][]string{
		`bond_james`		: []string{`Shaken, not stirred`, `Martinis`, `Women`},
		`moneypenny_miss`	: []string{`James Bond`, `Literature`, `Computer Science`},
		`no_dr`			: []string{`Being evil`, `Ice cream`, `Sunsets`},
	}

	m[`shital`] = []string{`hey`, `hi`, `how are you`}
	fmt.Println(m)

	delete(m, `no_dr`)
	fmt.Println(m)

	fmt.Println(m)
	for i, v := range m {
		fmt.Println(i)
		for j, x := range v {
			fmt.Println("\t", j, x)
		}
	}

}

