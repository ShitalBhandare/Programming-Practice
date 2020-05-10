package main

import (
	"fmt"
)

func main() {

	// INTRODUCTION:
	// The syntax for a map is map[key]value
	// maps are unordered
	// A map is the perfect data structure when you need to look up data fast.
	// Slices cannot be used as map keys, because equality is not defined on them.

	m := map[string]int{
		"Shital":24,
		"Preeti":25,
		"Dipa":16,		// Need this comma
	}
	fmt.Println(m)

	// Using key
	fmt.Println(m["Shital"])

	// An attempt to fetch a map value with a key that is not present in the map will return the zero value for the type of the entries in the map.
	fmt.Println(m["ABC"])

	// Comma OK idiom to figure out whether key actually present and its value is ZERO or not present at all.
	if v, ok := m["Dipa"]; ok {
		fmt.Printf("If key is present then value is %d\n", v)
	}

	// Adding an entry to map
	m["todd"] = 33
	fmt.Println(m)

	// Using range to loop over map
	for k, v := range m {
		fmt.Println(k, v)
	}

	// Deleting a key from map using delete built-in function.
	delete(m, "todd")
	fmt.Println(m)

	// Does not give any error if key is not present
	delete(m, "james")
	fmt.Println(m)

	// Delete using COMMA OK idiom
	if v, ok := m["Dipa"]; ok {
		fmt.Println(v)
		delete(m, "Dipa")
	}
	fmt.Println(m)

}


