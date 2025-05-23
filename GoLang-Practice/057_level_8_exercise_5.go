package main

import (
	"fmt"
	"sort"
)

type user struct {
	First   string
	Last    string
	Age     int
	Sayings []string
}

type ByAge []user

func (a ByAge) Len() int           { return len(a) }
func (a ByAge) Swap(i, j int)      { a[i], a[j] = a[j], a[i] }
func (a ByAge) Less(i, j int) bool { return a[i].Age < a[j].Age }

type ByLast []user

func (a ByLast) Len() int           { return len(a) }
func (a ByLast) Swap(i, j int)      { a[i], a[j] = a[j], a[i] }
func (a ByLast) Less(i, j int) bool { return a[i].Last < a[j].Last }

func main() {
	u1 := user{
		First: "James",
		Last:  "Bond",
		Age:   32,
		Sayings: []string{
			"Shaken, not stirred",
			"Youth is no guarantee of innovation",
			"In his majesty's royal service",
		},
	}

	u2 := user{
		First: "Miss",
		Last:  "Moneypenny",
		Age:   27,
		Sayings: []string{
			"James, it is soo good to see you",
			"Would you like me to take care of that for you, James?",
			"I would really prefer to be a secret agent myself.",
		},
	}

	u3 := user{
		First: "M",
		Last:  "Hmmmm",
		Age:   54,
		Sayings: []string{
			"Oh, James. You didn't.",
			"Dear God, what has James done now?",
			"Can someone please tell me where James Bond is?",
		},
	}

	users := []user{u1, u2, u3}
	for _, u := range users{
		fmt.Println(u.First, u.Last, u.Age)
		sort.Strings(u.Sayings)
		for _, v := range u.Sayings{
			fmt.Println("\t", v)
		}
	}

	fmt.Println("*****Sorting based on Age******")
	sort.Sort(ByAge(users))
	for _, u := range users{
		fmt.Println(u.First, u.Last, u.Age)
		for _, v := range u.Sayings{
			fmt.Println("\t", v)
		}
	}

	fmt.Println("*****Sorting based on Last******")
	sort.Sort(ByLast(users))
	for _, u := range users{
		fmt.Println(u.First, u.Last, u.Age)
		for _, v := range u.Sayings{
			fmt.Println("\t", v)
		}
	}

}

======================OUTPUT==================

James Bond 32
	 In his majesty's royal service
	 Shaken, not stirred
	 Youth is no guarantee of innovation
Miss Moneypenny 27
	 I would really prefer to be a secret agent myself.
	 James, it is soo good to see you
	 Would you like me to take care of that for you, James?
M Hmmmm 54
	 Can someone please tell me where James Bond is?
	 Dear God, what has James done now?
	 Oh, James. You didn't.
*****Sorting based on Age******
Miss Moneypenny 27
	 I would really prefer to be a secret agent myself.
	 James, it is soo good to see you
	 Would you like me to take care of that for you, James?
James Bond 32
	 In his majesty's royal service
	 Shaken, not stirred
	 Youth is no guarantee of innovation
M Hmmmm 54
	 Can someone please tell me where James Bond is?
	 Dear God, what has James done now?
	 Oh, James. You didn't.
*****Sorting based on Last******
James Bond 32
	 In his majesty's royal service
	 Shaken, not stirred
	 Youth is no guarantee of innovation
M Hmmmm 54
	 Can someone please tell me where James Bond is?
	 Dear God, what has James done now?
	 Oh, James. You didn't.
Miss Moneypenny 27
	 I would really prefer to be a secret agent myself.
	 James, it is soo good to see you
	 Would you like me to take care of that for you, James?

Program exited.
