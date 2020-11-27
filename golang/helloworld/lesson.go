package main // mainパッケージの用意が必要

import (
	"fmt"
	"strings"
)

func main() {
	fmt.Println("Hello World")
	fmt.Println("Hello " + "World")
	fmt.Println("Hello World"[0])
	fmt.Println(string("Hello World"[0]))

	var s string = "Hello World"
	fmt.Println(strings.Replace(s, "H", "X", 1))
	fmt.Println(s)
	s = strings.Replace(s, "H", "X", 1)

	fmt.Println(strings.Contains(s, "World"))

	fmt.Println(`Test
                                     Test
Test`)

	fmt.Println("\"")
	fmt.Println(`"`)
}
