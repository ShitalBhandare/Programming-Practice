package main

import (
	"fmt"
)

func main() {

	// Always check the errors
	// Unlike Python, Go does not have try, catch finally statements to catch exceptions.

	n, err := fmt.Println("Shital")
	if err != nil {
		fmt.Println(err)
		return
	}
	fmt.Println("No of bytes written:", n)

	var ans1, ans2, ans3 string

	fmt.Print("Fav Food:")
	_, err = fmt.Scan(&ans1)
	if err != nil {
		fmt.Println(err)
		return
	}

	fmt.Print("Fav Sport:")
	_, err = fmt.Scan(&ans2)
	if err != nil {
		fmt.Println(err)
		return
	}

	fmt.Print("Fav Drink:")
	_, err = fmt.Scan(&ans3)
	if err != nil {
		fmt.Println(err)
		return
	}
	fmt.Println(ans1, ans2, ans3)
}

=================OUTPUT=============

Shital
No of bytes written: 7
Fav Food:EOF
