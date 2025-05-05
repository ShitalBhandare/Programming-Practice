package main

import (
	"encoding/json"
	"fmt"
)

type person struct {
	First string				// If identifiers starts with small letter, it will not be exported in JSON encoding.
	Last  string
	Age   int
}

type employee struct {
	First string `json:"First"`		// Tag: `json:"First"` => customized json
	Last  string `json:"Last"`		// It specifies that json key "First" will point to Field "First" in Go
	Age   int    `json:"Age"`
}

func main() {

	p1 := person{
		First: "Shital",
		Last:  "Bhandare",
		Age:   24,
	}

	p2 := person{
		First: "Miss",
		Last:  "Monneypenny",
		Age:   32,
	}
	fmt.Println("\nBefore Marshalling")
	fmt.Println(p1, p2)


	// Marshal: Json encoding

	people := []person{p1, p2}
	bs, err := json.Marshal(people)
	if err != nil {
		fmt.Println("Failed to marshal, ", err)
	}
	fmt.Println("\nAfter Marshalling")
	fmt.Println(string(bs))



	// Unmarshal: JSON Decoding to Go Type

	var employees []employee
	err = json.Unmarshal(bs, &employees)
	if err != nil {
		fmt.Println(err)
	}
	fmt.Println("\nAfter Unmarshalling")
	fmt.Println(employees)

}


========================OUTPUT=====================

Before Marshalling
{Shital Bhandare 24} {Miss Monneypenny 32}

After Marshalling
[{"First":"Shital","Last":"Bhandare","Age":24},{"First":"Miss","Last":"Monneypenny","Age":32}]

After Unmarshalling
[{Shital Bhandare 24} {Miss Monneypenny 32}]
