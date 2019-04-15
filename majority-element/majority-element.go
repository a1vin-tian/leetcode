package main

func majorityElement(nums []int) int {
	var count int = 0
	var candidate int
	for _, n := range nums {
		if count == 0 {
			candidate = n
		}
		if candidate == n {
			count += 1
		} else {
			count += -1
		}
	}
	return candidate
}
