package kth_largest_element_in_an_array

import "testing"

func TestFindKthLargest(t *testing.T) {
	arr := []int{5, 4, 1, 4, 3}
	largest := FindKthLargest(arr, 2)
	t.Log(largest)
}
