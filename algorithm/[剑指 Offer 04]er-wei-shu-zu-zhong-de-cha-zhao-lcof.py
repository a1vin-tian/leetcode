# 在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个高效的函数，输入这样的一个二维数组和一个
# 整数，判断数组中是否含有该整数。 
# 
#  
# 
#  示例: 
# 
#  现有矩阵 matrix 如下： 
# 
#  
# [
#   [1,   4,  7, 11, 15],
#   [2,   5,  8, 12, 19],
#   [3,   6,  9, 16, 22],
#   [10, 13, 14, 17, 24],
#   [18, 21, 23, 26, 30]
# ]
#  
# 
#  给定 target = 5，返回 true。 
# 
#  给定 target = 20，返回 false。 
# 
#  
# 
#  限制： 
# 
#  0 <= n <= 1000 
# 
#  0 <= m <= 1000 
# 
#  
# 
#  注意：本题与主站 240 题相同：https://leetcode-cn.com/problems/search-a-2d-matrix-ii/ 
#  Related Topics 数组 二分查找 分治 矩阵 👍 427 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        """
        时间 O(mn)
        空间 O(1)

        顺时针旋转45度转成图，类似于二插搜索树

        :param matrix:
        :param target:
        :return:
        """
        i = len(matrix) - 1
        j = 0
        while i >= 0 and j < len(matrix[0]):
            if target == matrix[i][j]:
                return True
            elif target < matrix[i][j]:
                i -= 1
            elif target > matrix[i][j]:
                j += 1
        return False


# leetcode submit region end(Prohibit modification and deletion)

print(Solution().findNumberIn2DArray([[1]],1000))
