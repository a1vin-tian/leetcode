package main

import "fmt"

// 思路 此消彼长 x=全部数字  r=后半段数字的翻转 当 r >= x时说明已经过了 x的一半了 如果是偶数 x==r 如果是奇数则去掉最后一位判断相等
//  如:
// 1221 对比: 12 和21的翻转是否相同
//
// 12321 对比：12 123 / 10
// 问题:
// 怎么拿到每位的数字? 循环 r = x%10  x/10
// 怎么翻转？ r*10 + x%10
//
// 时间复杂度 O(N)
// 空间复杂度 O(1)

func isPalindrome(x int) bool {
	if x < 0 || (x != 0 && x%10 == 0) {
		return false
	}
	var r = 0
	for x > r {
		r = r*10 + x%10
		x /= 10
	}
	return r == x || r/10 == x
}

func main() {
	fmt.Print(isPalindrome(12321))
}
