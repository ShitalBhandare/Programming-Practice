package main

import (
	"fmt"
)


// A method is nothing more than a FUNC attached to a TYPE

type person struct{
	first string
	last string
}

// Syntax: func (r receiver) identifiere (parameters) (returns) { ... }

func (p person) speak(){
	fmt.Println(p.first, p.last, "can speak")
}

func main() {
	p1 := person{
		first: "Shital",
		last: "Bhandare",
	}

	p2 := person{
		first: "Mr",
		last: "Professor",
	}

	fmt.Println(p1)
	p1.speak()

	fmt.Println(p2)
	p2.speak()
}


