package main // mainパッケージの用意が必要

import "fmt"

func incrementGenerator() func() int {
	x := 0
	return func() int {
		x++
		return x
	}
}

func circleArea(pi float64) func(radius float64) float64 {
	return func(radius float64) float64 {
		return radius * radius * pi
	}

}

func main() {
	counter := incrementGenerator()
	fmt.Println(counter())
	fmt.Println(counter())
	fmt.Println(counter())

	c1 := circleArea(3.14)
	fmt.Println(c1(1))
	fmt.Println(c1(2))

	c2 := circleArea(3)
	fmt.Println(c2(1))
	fmt.Println(c2(2))

}
