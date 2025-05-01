package main

import (
	"fmt"
)

func main() {

	// Exercise 1
	array := [5]int{10, 20, 30, 40, 50}
	for i, v := range array {
		fmt.Println(i, v)
	}
	fmt.Printf("Type of array: %T\n", array)

	// Exercise 2
	slice := []int{42, 43, 44, 45, 46, 47, 48, 49, 50, 51}
	for i, v := range slice {
		fmt.Println(i, v)
	}
	fmt.Printf("Type of slice: %T\n", slice)

	// Exercise 3
	fmt.Println(slice[:5])
	fmt.Println(slice[5:])
	fmt.Println(slice[2:7])
	fmt.Println(slice[1:6])
	fmt.Println(slice)

	// Exercise 4
	x := []int{42, 43, 44, 45, 46, 47, 48, 49, 50, 51}
	x = append(x, 52)
	fmt.Println(x)
	x = append(x, 53, 54, 55)
	fmt.Println(x)

	y := []int{56, 57, 58, 59, 60}
	x = append(x, y...)
	fmt.Println(x)

	// Exercise 5 
	a := []int{42, 43, 44, 45, 46, 47, 48, 49, 50, 51}
	a = append(a[:2], a[6:]...)
	fmt.Println(a)

	// Exercise 6
	slice1 := make([]string, 50, 100)
	slice1 = []string{` Alabama`, ` Alaska`, ` Arizona`, ` Arkansas`, ` California`, ` Colorado`, ` Connecticut`, ` Delaware`, ` Florida`, ` Georgia`, ` Hawaii`, ` Idaho`, ` Illinois`, ` Indiana`, ` Iowa`, ` Kansas`, ` Kentucky`, ` Louisiana`, ` Maine`, ` Maryland`, ` Massachusetts`, ` Michigan`, ` Minnesota`, ` Mississippi`, ` Missouri`, ` Montana`, ` Nebraska`, ` Nevada`, ` New Hampshire`, ` New Jersey`, ` New Mexico`, ` New York`, ` North Carolina`, ` North Dakota`, ` Ohio`, ` Oklahoma`, ` Oregon`, ` Pennsylvania`, ` Rhode Island`, ` South Carolina`, ` South Dakota`, ` Tennessee`, ` Texas`, ` Utah`, ` Vermont`, ` Virginia`, ` Washington`, ` West Virginia`, ` Wisconsin`, ` Wyoming`}
	fmt.Println(slice1)
	fmt.Println(len(slice1))
	fmt.Println(cap(slice1))

	for i := 0; i < len(slice1); i++ {
		fmt.Println(i, slice1[i])
	}

	// Exercise 7

	s1 := []string{"James", "Bond", "Shaken, not stirred"}
	s2 := []string{"Miss", "Moneypenny", "Helloooooo, James."}

	s := [][]string{s1, s2}
	fmt.Println(s)

	for j := 0; j < len(s); j++ {
		fmt.Println(j, s[j])
		for k := 0; k < len(s[j]); k++ {
			fmt.Println(k, s[j][k])
		}
	}

	// Exercise 8
	m := map[string][]string{
		`bond_james`		: []string{`Shaken, not stirred`, `Martinis`, `Women`},
		`moneypenny_miss`	: []string{`James Bond`, `Literature`, `Computer Science`},
		`no_dr`			: []string{`Being evil`, `Ice cream`, `Sunsets`},
	}

	// Exercise 9
	m[`shital`] = []string{`hey`, `hi`, `how are you`}
	fmt.Println(m)

	// Exercise 10
	delete(m, `no_dr`)
	fmt.Println(m)

	fmt.Println(m)
	for i, v := range m {
		fmt.Println(i)
		for j, x := range v {
			fmt.Println("\t", j, x)
		}
	}

}


======================Output==================

0 10
1 20
2 30
3 40
4 50
Type of array: [5]int
0 42
1 43
2 44
3 45
4 46
5 47
6 48
7 49
8 50
9 51
Type of slice: []int
[42 43 44 45 46]
[47 48 49 50 51]
[44 45 46 47 48]
[43 44 45 46 47]
[42 43 44 45 46 47 48 49 50 51]
[42 43 44 45 46 47 48 49 50 51 52]
[42 43 44 45 46 47 48 49 50 51 52 53 54 55]
[42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60]
[42 43 48 49 50 51]
[ Alabama  Alaska  Arizona  Arkansas  California  Colorado  Connecticut  Delaware  Florida  Georgia  Hawaii  Idaho  Illinois  Indiana  Iowa  Kansas  Kentucky  Louisiana  Maine  Maryland  Massachusetts  Michigan  Minnesota  Mississippi  Missouri  Montana  Nebraska  Nevada  New Hampshire  New Jersey  New Mexico  New York  North Carolina  North Dakota  Ohio  Oklahoma  Oregon  Pennsylvania  Rhode Island  South Carolina  South Dakota  Tennessee  Texas  Utah  Vermont  Virginia  Washington  West Virginia  Wisconsin  Wyoming]
50
50
0  Alabama
1  Alaska
2  Arizona
3  Arkansas
4  California
5  Colorado
6  Connecticut
7  Delaware
8  Florida
9  Georgia
10  Hawaii
11  Idaho
12  Illinois
13  Indiana
14  Iowa
15  Kansas
16  Kentucky
17  Louisiana
18  Maine
19  Maryland
20  Massachusetts
21  Michigan
22  Minnesota
23  Mississippi
24  Missouri
25  Montana
26  Nebraska
27  Nevada
28  New Hampshire
29  New Jersey
30  New Mexico
31  New York
32  North Carolina
33  North Dakota
34  Ohio
35  Oklahoma
36  Oregon
37  Pennsylvania
38  Rhode Island
39  South Carolina
40  South Dakota
41  Tennessee
42  Texas
43  Utah
44  Vermont
45  Virginia
46  Washington
47  West Virginia
48  Wisconsin
49  Wyoming
[[James Bond Shaken, not stirred] [Miss Moneypenny Helloooooo, James.]]
0 [James Bond Shaken, not stirred]
0 James
1 Bond
2 Shaken, not stirred
1 [Miss Moneypenny Helloooooo, James.]
0 Miss
1 Moneypenny
2 Helloooooo, James.
map[bond_james:[Shaken, not stirred Martinis Women] moneypenny_miss:[James Bond Literature Computer Science] no_dr:[Being evil Ice cream Sunsets] shital:[hey hi how are you]]
map[bond_james:[Shaken, not stirred Martinis Women] moneypenny_miss:[James Bond Literature Computer Science] shital:[hey hi how are you]]
map[bond_james:[Shaken, not stirred Martinis Women] moneypenny_miss:[James Bond Literature Computer Science] shital:[hey hi how are you]]
bond_james
	 0 Shaken, not stirred
	 1 Martinis
	 2 Women
moneypenny_miss
	 0 James Bond
	 1 Literature
	 2 Computer Science
shital
	 0 hey
	 1 hi
	 2 how are you
