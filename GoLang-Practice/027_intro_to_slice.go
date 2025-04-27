package main

import "fmt"

func main() {

	// Composite Literal
	// SLICE allows you to group values of SAME TYPE


	slice := []int {1, 2, 3, 4, 5}
	fmt.Println(slice)
	fmt.Println(len(slice))

	// Iterate over slice using range clause
	// i:index, v:value
	for i, v := range slice {
		fmt.Println(i, v)
	}

	// Slicing a slice
	fmt.Println(slice[:])
	fmt.Println(slice[1:])
	fmt.Println(slice[1:4])

	x := []int{1, 2, 3, 4}
	fmt.Println(x)

	// Appending values to slice
	x = append(x, 5, 6, 7, 8)
	fmt.Println(x)

	//Appending a slice to slice
	y := []int{9, 10, 11, 12}
	x = append(x, y...)	// y... => It will take all values from slice one by one
	fmt.Println(x)
	// Below will raise an error since y is not of type int
	// x = append(x, y)

	// Deleting from a slice
	x = append(x[:3], x[7:9]...)
	fmt.Println(x)

	// Slice is dynamic in nature. Slice is built on top of array.
	// Whenver, you append/delete element from an array, length of an underlying array is changed.
	// Underlying array is thrown out and created a new array with new length.
	// But it requires some processing time as it does at runtime.
	// To reduce this overhead, we can create slice using make built-in function


	// Creating slice using built-in make function
	s := make([]int, 5, 10)
	fmt.Println(s)
	fmt.Println(len(s))		// len => length of slice
	fmt.Println(cap(s))		// cap => capacity of underlying array

	s = append(s, 6, 7, 8, 9, 10)
	fmt.Println(s)
	fmt.Println(len(s))
	fmt.Println(cap(s))

	s = append(s, 11, 22, 33, 44)
	fmt.Println(s)
	fmt.Println(len(s))
	fmt.Println(cap(s))		// Capacity gets doubled of existing capacity when underlying array is full.

	s = append(s, 55, 66, 77, 88, 99, 100, 200, 300, 400)
	fmt.Println(s)
	fmt.Println(len(s))
	fmt.Println(cap(s))

	// Multi-dimentional slices

	slice1 := []string{"Shital", "Bhandare", "Vita"}
	fmt.Println(slice1)

	slice2 := []string{"abc", "xyz", "nowhere"}
	fmt.Println(slice2)

	multi_slice := [][]string{slice1, slice2}
	fmt.Println(multi_slice)
}



======================OUTPUT===================

[1 2 3 4 5]
5
0 1
1 2
2 3
3 4
4 5
[1 2 3 4 5]
[2 3 4 5]
[2 3 4]
[1 2 3 4]
[1 2 3 4 5 6 7 8]
[1 2 3 4 5 6 7 8 9 10 11 12]
[1 2 3 8 9]
[0 0 0 0 0]
5
10
[0 0 0 0 0 6 7 8 9 10]
10
10
[0 0 0 0 0 6 7 8 9 10 11 22 33 44]
14
20
[0 0 0 0 0 6 7 8 9 10 11 22 33 44 55 66 77 88 99 100 200 300 400]
23
40
[Shital Bhandare Vita]
[abc xyz nowhere]
[[Shital Bhandare Vita] [abc xyz nowhere]]

Program exited.
