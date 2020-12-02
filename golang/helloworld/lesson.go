package main // mainパッケージの用意が必要

import "fmt"

func my_print(var_name string, val []int) {
	fmt.Printf("["+var_name+"] len=%d cap=%d value=%v\n", len(val), cap(val), val)
}

func main() {

	n := make([]int, 3, 5)
	my_print("n", n)

	n1 := append(n, 0, 0)
	my_print("n", n)
	my_print("n1", n1)

	n2 := append(n1, 1, 2, 3, 4, 5)
	my_print("n2", n2)

	a := make([]int, 3)
	my_print("a", a)

	b := make([]int, 0)
	var c []int
	my_print("b", b)
	my_print("c", c)

	c = make([]int, 0, 5)
	for i := 0; i < 5; i++ {
		c = append(c, i)
		fmt.Println(c)
	}
	fmt.Println(c)

}
