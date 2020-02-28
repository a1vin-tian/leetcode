package main

import "fmt"

//给定一个字符串，逐个翻转字符串中的每个单词。
//
// 
//
// 示例 1： 
//
// 输入: "the sky is blue"
//输出: "blue is sky the"
// 
//
// 示例 2： 
//
// 输入: "  hello world!  "
//输出: "world! hello"
//解释: 输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
// 
//
// 示例 3： 
//
// 输入: "a good   example"
//输出: "example good a"
//解释: 如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。
// 
//
// 
//
// 说明： 
//
// 
// 无空格字符构成一个单词。 
// 输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。 
// 如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。 
// 
//
// 
//
// 进阶： 
//
// 请选用 C 语言的用户尝试使用 O(1) 额外空间复杂度的原地解法。 
// Related Topics 字符串

//leetcode submit region begin(Prohibit modification and deletion)
func reverseWords(s string) string {
	b := []byte(s)
	reverse(b, 0, len(s)-1)
	reverseWord(b)
	return string(cleanSpace(b))
}

func cleanSpace(s []byte) []byte {
	i, j, n := 0, 0, len(s)
	for j < n {
		for j < n && s[j] == ' ' {
			j++
		}
		for j < n && s[j] != ' ' {
			s[i] = s[j]
			i++
			j++
		}
		for j < n && s[j] == ' ' {
			j++
		}
		if j < n {
			s[i] = ' '
			i++
		}
	}
	return s[:i]
}

func reverseWord(s []byte) {
	i, j, n := 0, 0, len(s)
	for i < n {
		for i < j || i < n && s[i] == ' ' {
			i++
		}
		for j < i || j < n && s[j] != ' ' {
			j++
		}
		reverse(s, i, j-1)
	}
}

func reverse(s []byte, i, j int) {
	for i < j {
		s[i], s[j] = s[j], s[i]
		i++
		j--
	}
}

//leetcode submit region end(Prohibit modification and deletion)

func main() {
	fmt.Printf("%v", reverseWords("  hello world!  "))
}
