package Saying

import "testing"
import "fmt"

func TestGreet(t *testing.T) {
	s := Greet("Shital")
	if s != "Hey, Shital" {
		t.Error("Got ", s, "Expected ", "Hey, Shital")
	}
}

func ExampleGreet() {
	s := Greet("Shital")
	fmt.Println(s)
	// Output:
	// Hey, Shital

}

func BenchmarkGreet(b *testing.B) {
	for i := 0; i < b.N; i++ {
		Greet("Shital")
	}
}
