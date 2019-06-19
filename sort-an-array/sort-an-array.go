package sort_an_array

func sortArray(arr []int) []int {
	if arr == nil || len(arr) == 0 {
		return arr
	}
	mergeSort(arr, 0, len(arr)-1)
	return arr
}

func mergeSort(arr []int, start int, end int) {
	if start >= end {
		return
	}
	mid := (start + end) / 2
	mergeSort(arr, start, mid)
	mergeSort(arr, mid+1, end)
	merge(arr, start, mid, end)
}

func merge(arr []int, start, mid, end int) {
	tmp := make([]int, end-start+1)
	i := start
	j := mid + 1
	k := 0
	for ; i <= mid && j <= end; k++ {
		if arr[i] < arr[j] {
			tmp[k] = arr[i]
			i++
		} else {
			tmp[k] = arr[j]
			j++
		}
	}
	s := i
	e := mid
	if j <= end {
		s = j
		e = end
	}

	for ; s <= e; {
		tmp[k] = arr[s]
		k++
		s++
	}
	copy(arr[start:end+1], tmp)
}
