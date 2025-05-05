package main

import (
	"fmt"
	"sort"
)

func main() {
	xi := []int{5, 8, 2, 43, 17, 987, 14, 12, 21, 1, 4, 2, 3, 93, 13}
	xs := []string{"random", "rainbow", "delights", "in", "torpedo", "summers", "under", "gallantry", "fragmented", "moons", "across", "magenta"}

	fmt.Println(xi)
	// sort xi
	sort.Ints(xi)
	fmt.Println(xi)

	fmt.Println(xs)
	// sort xs
	sort.Strings(xs)
	fmt.Println(xs)

}

================OUTPUT=============

[5 8 2 43 17 987 14 12 21 1 4 2 3 93 13]
[1 2 2 3 4 5 8 12 13 14 17 21 43 93 987]
[random rainbow delights in torpedo summers under gallantry fragmented moons across magenta]
[across delights fragmented gallantry in magenta moons rainbow random summers torpedo under]

Program exited.

