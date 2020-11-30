package main // mainパッケージの用意が必要

import (
	"fmt"
)

func main() {

	// array
	var a [2]int
	a[0] = 100
	a[1] = 200
	fmt.Println(a)

	/*
		// array
		var b [2]int = [2]int{100, 200}
		fmt.Println(b)
	*/
	// slice
	// slice can be append.
	var b []int = []int{100, 200}
	b = append(b, 300)
	fmt.Println(b)
}
