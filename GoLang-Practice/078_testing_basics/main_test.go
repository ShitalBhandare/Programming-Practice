package main

import "testing"

func TestMySub(t *testing.T) {
	sub := mySub(5, 3)
	if sub != 2 {
		t.Error("Expected", 2, "Got", sub)
	}
}
