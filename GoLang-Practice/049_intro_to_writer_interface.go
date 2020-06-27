package main

import (
	"fmt"
	"io"
	"os"
)

func main() {
	fmt.Println("Hey, there")

	//fmt.Println internally implements fmt.Fprintln()
	// os.Stdout => writer
	fmt.Fprintln(os.Stdout, "Hey, there")

	io.WriteString(os.Stdout, "Hey, there")
}
