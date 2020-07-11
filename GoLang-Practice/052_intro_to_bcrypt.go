package main

import (
	"fmt"
	"golang.org/x/crypto/bcrypt"
)

func main() {
	password := `passord123`
	fmt.Println(password)
	bs, err := bcrypt.GenerateFromPassword([]byte(password), bcrypt.MinCost)
	if err != nil {
		fmt.Println("Cannot generate password")
		return
	}
	fmt.Println(bs)

	new_password := `password123`
	err = bcrypt.CompareHashAndPassword(bs, []byte(new_password))
	if err != nil {
                fmt.Println("passwords do not match")
                return
        }
	fmt.Println("Password matches")

}
