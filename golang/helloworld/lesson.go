package main // mainパッケージの用意が必要

import (
	"fmt"
	"strconv"
)

func main() {

	var x int = 1
	xx := float64(x)
	fmt.Printf("%T %v %f\n", xx, xx, xx)

	var y float64 = 1.2
	yy := int(y)
	fmt.Printf("%T %v %d\n", yy, yy, yy)

	i, _ := strconv.Atoi("14")
	fmt.Printf("%T %v\n", i, i)

	h := "Hello World"
	fmt.Printf("%T %v\n", h[0], h[0])
	fmt.Printf("%T %v\n", string(h[0]), string(h[0]))
}
