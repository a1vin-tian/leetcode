package kth_largest_element_in_an_array

func FindKthLargest(nums []int, k int) int {
	return findKthLargest(nums, k)
}

func findKthLargest(nums []int, k int) int {
	k = len(nums) - k
	lo := 0
	hi := len(nums) - 1
	for ; lo < hi; {
		j := partition(nums, lo, hi)
		if j < k {
			lo = j + 1
		} else if j > k {
			hi = j - 1
		} else {
			break
		}
	}
	return nums[k]
}

func partition(arr []int, start, end int) int {
	pivot := arr[end]
	i := start

	for j := start; j < end; j++ {
		if arr[j] < pivot {
			if i != j {
				arr[i], arr[j] = arr[j], arr[i]
			}
			i++
		}
	}
	arr[i], arr[end] = arr[end], arr[i]
	return i
}
