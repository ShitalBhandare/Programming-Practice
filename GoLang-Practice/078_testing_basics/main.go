package main

import "fmt"

func main(){
	sub := mySub(5, 3)
	fmt.Println("Subtraction:", sub)
}

func mySub(x int, y int) int {
	return x - y

}
