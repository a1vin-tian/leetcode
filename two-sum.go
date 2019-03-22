package main

import "fmt"

/**
空间换时间
 */
func twoSum(nums []int, target int) []int {
	var m = make(map[int]int)
	m[nums[0]] = 0
	for i := 1; i < len(nums); i++ {
		var c = target - nums[i]
		if n, ok := m[c]; ok {
			return []int{n, i}
		} else {
			m[nums[i]] = i
		}
	}
	return nil
}

func main() {
	fmt.Print(twoSum([]int{2, 7, 11, 15}, 9))
}
