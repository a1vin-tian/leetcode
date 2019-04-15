package main

func majorityElement(nums []int) []int {
	var count1, count2, candidate1, candidate2 int = 0, 0, 0, 0
	for _, n := range nums {
		if n == candidate1 {
			count1++;
		} else if n == candidate2 {
			count2 ++;
		} else if count1 == 0 {
			candidate1, count1 = n, 1
		} else if count2 == 0 {
			candidate2, count2 = n, 1
		} else {
			count1--
			count2--
		}
	}
	count1, count2 = 0, 0
	for _, n := range nums {
		if n == candidate1 {
			count1++;
		} else if n == candidate2 {
			count2 ++;
		}
	}
	var result []int
	if count1 > len(nums)/3 {
		result = append(result, candidate1)
	}
	if count2 > len(nums)/3 {
		result = append(result, candidate2)
	}
	return result
}
