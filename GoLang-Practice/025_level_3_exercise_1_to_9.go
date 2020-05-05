package main

import "fmt"

func main(){
	for i := 1; i <= 10000; i++ {
		fmt.Println(i)
	}

	for i := 65; i <= 90; i++ {
		fmt.Println(i)
		for j := 0; j < 3; j++ {
			fmt.Printf("\t%#U\n", i)
		}
	}

	year := 1995
	for year <= 2020 {
		fmt.Println(year)
		year++
	}

	year = 1995
	for {
		if year <= 2020 {
			fmt.Println(year)
			year++
		} else {
			break
		}
	}

	for k := 10; k <= 100; k++ {
		fmt.Printf("When %d is divided by 4, the remainder is %d\n", k, k % 4)
	}

	str := "Shital"
	if str == "shital" {
		fmt.Println("its name")
	} else if str == "bhandare" {
		fmt.Println("Its surname")
	} else {
		fmt.Println("No match present")
	}

	switch {
	case (2 != 2):
		fmt.Println("False")
	case (4 == 4):
		fmt.Println("True")
	}

	favSport := "Badminton"
	switch favSport {
	case "Badminton":
		fmt.Println("Its Badminton")
	case "Carrom":
		fmt.Println("Its Carrom")
	case "Pool":
		fmt.Println("Its Pool")
	}

	fmt.Println("true && true: ",true && true)
	fmt.Println("true && false: ", true && false)
	fmt.Println("true || true: ", true || true)
	fmt.Println("true || false: ", true || false)
	fmt.Println("!true: ", !true)


}
