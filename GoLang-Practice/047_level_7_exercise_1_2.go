package main

import "fmt"

type person struct{
	first string
	last string
	age int
}

func changeMe(p *person){
	//(*p).first = "James"
	p.first = "James"		// This works
	(*p).last = "Bond"
	(*p).age = 34
}


func main() {

	// Exercise 1
	x := 20
	fmt.Println("x:\t", x)
	fmt.Println("&x:\t", &x)

	// Exercise 2
	p := person{
		first: "Shital",
		last: "Bhandare",
		age: 24,
	}
	fmt.Println(p)
	changeMe(&p)
	fmt.Println(p)
}


============OUTPUT==========

x:	 20
&x:	 0xc00008a040
{Shital Bhandare 24}
{James Bond 34}
