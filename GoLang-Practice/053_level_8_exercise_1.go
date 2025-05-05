package main

import (
	"encoding/json"
	"fmt"
)

type user struct {
	First string
	Age   int
}

func main() {
	u1 := user{
		First: "James",
		Age:   32,
	}

	u2 := user{
		First: "Moneypenny",
		Age:   27,
	}

	u3 := user{
		First: "M",
		Age:   54,
	}

	users := []user{u1, u2, u3}

	fmt.Println(users)

	// your code goes here
	bs, err := json.Marshal(users)
	if err != nil {
		fmt.Println("Unable to marshal the data")
	}
	fmt.Println(bs)
	fmt.Println(string(bs))
}

======================OUTPUT==================


[{James 32} {Moneypenny 27} {M 54}]
[91 123 34 70 105 114 115 116 34 58 34 74 97 109 101 115 34 44 34 65 103 101 34 58 51 50 125 44 123 34 70 105 114 115 116 34 58 34 77 111 110 101 121 112 101 110 110 121 34 44 34 65 103 101 34 58 50 55 125 44 123 34 70 105 114 115 116 34 58 34 77 34 44 34 65 103 101 34 58 53 52 125 93]
[{"First":"James","Age":32},{"First":"Moneypenny","Age":27},{"First":"M","Age":54}]
