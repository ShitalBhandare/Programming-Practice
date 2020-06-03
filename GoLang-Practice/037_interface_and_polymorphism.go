package main

import (
        "fmt"
)


// Interface, Polymorphism, Conversion and Assertion

type person struct{
        first string
        last string
}

type employee struct{
	person
	id int
}

// Syntax: func (r receiver) identifiere (parameters) (returns) { ... }

func (p person) speak(){
        fmt.Println(p.first, p.last, "can speak")
}

func (e employee) speak(){
	fmt.Println(e.first, e.last, "can speak")
}

// Intro to interface
type human interface{
	speak()
}


func bar(h human) {
	switch h.(type){
	case person:
		fmt.Println("Called into bar for", h.(person).first, h.(person).last)		// ASSERTION
	case employee:
		fmt.Println("Called into bar for", h.(employee).first, h.(employee).last)
	}
}

// A VALUE CAN BE OF MORE THAN ONE TYPE

func main() {
        p1 := person{
                first: "Shital",
                last: "Bhandare",
        }

        p2 := person{
                first: "Mr",
                last: "Professor",
        }

	e1 := employee{
		person: person{
			first: "Miss",
			last: "Tokyo",
		},
		id: 1873,
	}

        fmt.Println(p1)
        p1.speak()

        fmt.Println(p2)
        p2.speak()

	fmt.Println(e1)
	e1.speak()


	// Polymorphism
	// Different values like person and employee passed in to bar()
	bar(p1)
	bar(p2)
	bar(e1)

	type hotdog int
	var x hotdog
	x = 42
	fmt.Printf("%T, %v\n", x, x)
	y := int(x)					// Conversion
	fmt.Printf("%T, %v\n", y, y)
}

