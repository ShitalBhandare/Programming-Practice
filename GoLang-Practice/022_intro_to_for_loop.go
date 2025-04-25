package main

import (
	"fmt"
)

func main() {

	// for initial; condition; post
	for i := 0; i < 5; i++ {
		fmt.Println(i)
	}

	// Nested Loop
	for i := 0; i < 5; i++ {
		fmt.Printf("The outer loop: %d\n", i)
		for j := 0; j < 3; j++ {
			fmt.Printf("\t\tThe innerr loop: %d\n", j)
		}
	}

	// Like C (;;) Usage of break and continue
	i := 1
	for {
		i++
		if i > 20 {
			break
		}
		if i % 2 == 1 {
			continue
		}
		fmt.Println(i)

	}

	// Similar to while loop
	j := 1
        for j < 15 {
		j = j*2
                fmt.Println(j)
        }

	// Printing ASCII values
	for i := 33; i < 122; i++ {
		fmt.Printf("%v\t\t%#U\n", i, i)
	}
}


===================OUTPUT==================


0
1
2
3
4
The outer loop: 0
		The innerr loop: 0
		The innerr loop: 1
		The innerr loop: 2
The outer loop: 1
		The innerr loop: 0
		The innerr loop: 1
		The innerr loop: 2
The outer loop: 2
		The innerr loop: 0
		The innerr loop: 1
		The innerr loop: 2
The outer loop: 3
		The innerr loop: 0
		The innerr loop: 1
		The innerr loop: 2
The outer loop: 4
		The innerr loop: 0
		The innerr loop: 1
		The innerr loop: 2
2
4
6
8
10
12
14
16
18
20
2
4
8
16
33		U+0021 '!'
34		U+0022 '"'
35		U+0023 '#'
36		U+0024 '$'
37		U+0025 '%'
38		U+0026 '&'
39		U+0027 '''
40		U+0028 '('
41		U+0029 ')'
42		U+002A '*'
43		U+002B '+'
44		U+002C ','
45		U+002D '-'
46		U+002E '.'
47		U+002F '/'
48		U+0030 '0'
49		U+0031 '1'
50		U+0032 '2'
51		U+0033 '3'
52		U+0034 '4'
53		U+0035 '5'
54		U+0036 '6'
55		U+0037 '7'
56		U+0038 '8'
57		U+0039 '9'
58		U+003A ':'
59		U+003B ';'
60		U+003C '<'
61		U+003D '='
62		U+003E '>'
63		U+003F '?'
64		U+0040 '@'
65		U+0041 'A'
66		U+0042 'B'
67		U+0043 'C'
68		U+0044 'D'
69		U+0045 'E'
70		U+0046 'F'
71		U+0047 'G'
72		U+0048 'H'
73		U+0049 'I'
74		U+004A 'J'
75		U+004B 'K'
76		U+004C 'L'
77		U+004D 'M'
78		U+004E 'N'
79		U+004F 'O'
80		U+0050 'P'
81		U+0051 'Q'
82		U+0052 'R'
83		U+0053 'S'
84		U+0054 'T'
85		U+0055 'U'
86		U+0056 'V'
87		U+0057 'W'
88		U+0058 'X'
89		U+0059 'Y'
90		U+005A 'Z'
91		U+005B '['
92		U+005C '\'
93		U+005D ']'
94		U+005E '^'
95		U+005F '_'
96		U+0060 '`'
97		U+0061 'a'
98		U+0062 'b'
99		U+0063 'c'
100		U+0064 'd'
101		U+0065 'e'
102		U+0066 'f'
103		U+0067 'g'
104		U+0068 'h'
105		U+0069 'i'
106		U+006A 'j'
107		U+006B 'k'
108		U+006C 'l'
109		U+006D 'm'
110		U+006E 'n'
111		U+006F 'o'
112		U+0070 'p'
113		U+0071 'q'
114		U+0072 'r'
115		U+0073 's'
116		U+0074 't'
117		U+0075 'u'
118		U+0076 'v'
119		U+0077 'w'
120		U+0078 'x'
121		U+0079 'y'

Program exited.
About the Playground
