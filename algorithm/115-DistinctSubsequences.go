package main

import "fmt"

//给定一个字符串 S 和一个字符串 T，计算在 S 的子序列中 T 出现的个数。
//
// 一个字符串的一个子序列是指，通过删除一些（也可以不删除）字符且不干扰剩余字符相对位置所组成的新字符串。（例如，"ACE" 是 "ABCDE" 的一个子序列
//，而 "AEC" 不是） 
//
// 示例 1: 
//
// 输入: S = "rabbbit", T = "rabbit"
//输出: 3
//解释:
//
//如下图所示, 有 3 种可以从 S 中得到 "rabbit" 的方案。
//(上箭头符号 ^ 表示选取的字母)
//
//rabbbit
//^^^^ ^^
//rabbbit
//^^ ^^^^
//rabbbit
//^^^ ^^^
// 
//
// 示例 2: 
//
// 输入: S = "babgbag", T = "bag"
//输出: 5
//解释:
//
//如下图所示, 有 5 种可以从 S 中得到 "bag" 的方案。 
//(上箭头符号 ^ 表示选取的字母)
//
//babgbag
//^^ ^
//babgbag
//^^    ^
//babgbag
//^    ^^
//babgbag
//  ^  ^^
//babgbag
//    ^^^ 
// Related Topics 字符串 动态规划

//leetcode submit region begin(Prohibit modification and deletion)

func numDistinct(s string, t string) int {
	// dp[i][j] = s[0..j-1]与t[0..i]的子序列的总数
	// dp方程:
	m, n := len(t), len(s)
	dp := *make2d(m+1, n+1)
	for i := 0; i < n+1; i++ {
		dp[0][i] = 1
	}
	for i := 1; i < m+1; i++ {
		for j := 1; j < n+1; j++ {
			if s[j-1] == t[i-1] {
				dp[i][j] = dp[i-1][j-1] + dp[i][j-1]
			} else {
				dp[i][j] = dp[i][j-1]
			}
		}
	}
	return dp[m][n]
}

func make2d(m int, n int) *[][]int {
	dp := make([][]int, m)
	for i := 0; i < m; i++ {
		dp[i] = make([]int, n)
	}
	return &dp
}

//leetcode submit region end(Prohibit modification and deletion)

func main() {
	fmt.Printf("%v", numDistinct("rabbbit",
		"rabbit"))
}
