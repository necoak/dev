package main // mainパッケージの用意が必要

import "fmt"

func calc(x int, y int) (int, int) {
	return x + y, x - y
}

func calc2(price int, item int) (result int) {
	result = price * item
	// return result
	return
}

func main() {
	r1, r2 := calc(10, 20)
	fmt.Println(r1, r2)

	r3 := calc2(100, 2)
	fmt.Println(r3)
}
