package main

import (
	"fmt"
)

type person struct {
	first      string
	last       string
	fav_flavor []string
}

func main() {
	// Exercise 1
	fmt.Println("Exercise 1 Output")
	p1 := person{
		first: "shital",
		last:  "bhandare",
		fav_flavor: []string{
			"gulkand",
			"vanilla",
		},
	}
	p2 := person{
		first: "priti",
		last:  "gurav",
		fav_flavor: []string{
			"butterscotch",
			"vanilla",
		},
	}
	fmt.Println(p1.first)
	fmt.Println(p1.last)
	for i, v := range p1.fav_flavor {
		fmt.Println(i, v)
	}

	fmt.Println(p2.first)
	fmt.Println(p2.last)
	for i, v := range p2.fav_flavor {
		fmt.Println(i, v)
	}

	// Exercise 2
	fmt.Println("\nExercise 2 Output")
	m := map[string]person{
		p1.last: p1,
		p2.last: p2,
	}

	for _, v := range m {
		fmt.Println(v.first)
		fmt.Println(v.last)
		for i, v := range v.fav_flavor {
			fmt.Println(i, v)
		}
		fmt.Println("------")
	}

	type vehicle struct {
		doors int
		color string
	}

	type truck struct {
		vehicle
		fourWheel bool
	}

	type sedan struct {
		vehicle
		luxury bool
	}

	// Exercise 3
	fmt.Println("\nExercise 3 Output")

	truck1 := truck{
		vehicle: vehicle{
			doors: 2,
			color: "red",
		},
		fourWheel: true,
	}

	sedan1 := sedan{
		vehicle: vehicle{
			doors: 4,
			color: "black",
		},
		luxury: false,
	}
	fmt.Println("Truck Info:", truck1)

	fmt.Println(truck1.vehicle.doors) // fmt.Println(truck1.doors) also works
	fmt.Println(truck1.vehicle.color)
	fmt.Println(truck1.fourWheel)

	fmt.Println("Sedan Info:", sedan1)

	fmt.Println(sedan1.vehicle.doors)
	fmt.Println(sedan1.vehicle.color)
	fmt.Println(sedan1.luxury)

	// Exercise 4

	fmt.Println("Exercise 4 Output:")

	e1 := struct {
		id   int
		name string
	}{
		id:   1,
		name: "shital bhandare",
	}
	fmt.Println(e1.id, e1.name)

}

