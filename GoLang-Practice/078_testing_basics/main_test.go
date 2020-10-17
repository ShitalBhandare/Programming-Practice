package main

import "testing"

func TestMySum(t *testing.T) {

	type test struct{
		data []int
		answer int
	}

	//Table tests: series of tests
	tests := []test{
		test{[]int{1, 2}, 3},
		test{[]int{-1, -4}, -5},
		test{[]int{5, 3}, 8},
	}

	for _, v := range tests {
		sum := mySum(v.data...)
	        if sum != v.answer {
			t.Error("Expected", v.answer, "Got", sum)
		}


	}

}
