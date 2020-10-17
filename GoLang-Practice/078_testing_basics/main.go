package main

import "fmt"

func main(){
	xi := []int{8, 4}
	sum := mySum(xi...)
	fmt.Println("Addition:", sum)
}

func mySum(xi ...int) int {
	sum := 0
	for _, v := range xi {
		sum = sum + v
	}
	return sum

}
