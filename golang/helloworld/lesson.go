package main // mainパッケージの用意が必要

import (
	"fmt"
)

func main() {
	var t, f bool = true, false
	//t, f := true, false // これでもいい
	fmt.Printf("%T %v\n", t, t)
	fmt.Printf("%T %v\n", f, f)

	fmt.Printf("%T %v %t\n", 0, 0, 0)
	fmt.Printf("%T %v %t\n", 1, 1, 1)

	fmt.Println(true && true)
	fmt.Println(true && false)
	fmt.Println(false && false)

	fmt.Println(true || true)
	fmt.Println(true || false)
	fmt.Println(false || false)

	fmt.Println(!true)
	fmt.Println(!false)
}
