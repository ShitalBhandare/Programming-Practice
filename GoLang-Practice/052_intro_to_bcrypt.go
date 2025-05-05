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


========================OUTPUT================

passord123
[36 50 97 36 48 52 36 112 101 117 106 48 101 67 72 108 119 102 47 107 73 108 85 111 50 89 78 110 101 77 82 111 119 75 72 108 121 69 74 122 87 103 48 57 72 99 114 85 90 82 122 89 112 99 79 54 73 79 97 117]
passwords do not match
