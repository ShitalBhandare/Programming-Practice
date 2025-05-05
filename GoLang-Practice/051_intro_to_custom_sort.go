package main

import (
	"fmt"
	"sort"
)

// Custom Sorting

type Person struct {
	First string
	Age   int
}

// ByAge implements sort.Interface for []Person based on the Age field.

type ByAge []Person

func (a ByAge) Len() int           { return len(a) }
func (a ByAge) Swap(i, j int)      { a[i], a[j] = a[j], a[i] }
func (a ByAge) Less(i, j int) bool { return a[i].Age < a[j].Age }

// ByName implements sort.Interface for []Person based on the Name field.

type ByName []Person

func (a ByName) Len() int           { return len(a) }
func (a ByName) Swap(i, j int)      { a[i], a[j] = a[j], a[i] }
func (a ByName) Less(i, j int) bool { return a[i].First < a[j].First }

func main() {

	person1 := Person{First: "Shital", Age: 24}
	person2 := Person{First: "Ameya", Age: 30}
	person3 := Person{First: "Prasad", Age: 26}
	person4 := Person{First: "James", Age: 34}

	people := []Person{person1, person2, person3, person4}

	fmt.Println("Without Sorting:", people)

	sort.Sort(ByAge(people))
	fmt.Println("\nSorting By Age:", people)

	sort.Sort(ByName(people))
	fmt.Println("\nSorting By Name:", people)

}


=====================output=============

Without Sorting: [{Shital 24} {Ameya 30} {Prasad 26} {James 34}]

Sorting By Age: [{Shital 24} {Prasad 26} {Ameya 30} {James 34}]

Sorting By Name: [{Ameya 30} {James 34} {Prasad 26} {Shital 24}]

Program exited.
