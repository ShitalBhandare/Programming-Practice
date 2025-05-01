package main

import (
	"fmt"
)

// STRUCT: Composite Data Type which holds values of different type
// TYPE person with underlined data type struct

type person struct{
	first string
	last string
	age int
}

// Embedded struct

type employee struct{
	person
	emp_id int
}

func main() {

	p1 := person{
		first: "Shital",
		last: "Bhandare",
		age: 24,
	}
	fmt.Println(p1)
	fmt.Println(p1.first, p1.last, p1.age)

	e1 := employee{
		person : person{
			first: "ABC",
			last: "XYZ",
			age: 32,
		},
		emp_id: 1873,
	}

	fmt.Println(e1)
	fmt.Println(e1.person, e1.emp_id)

	// To resolve the name collision
	fmt.Println(e1.person.first, e1.person.last, e1.person.age, e1.emp_id)

	// Anonymous struct
	// Can be used to avoid code pollution

	person1 := struct {
		first string
		last  string
		age   int
	}{
		first: "Shital",
		last:  "Bhandare",
		age:   24,
	}
	fmt.Println(person1)
}

===========OUTPUT========

{Shital Bhandare 24}
Shital Bhandare 24
{{ABC XYZ 32} 1873}
{ABC XYZ 32} 1873
ABC XYZ 32 1873
{Shital Bhandare 24}
