# 在一个 2 x 3 的板上（board）有 5 块砖瓦，用数字 1~5 来表示, 以及一块空缺用 0 来表示.
#
# 一次移动定义为选择 0 与一个相邻的数字（上下左右）进行交换.
#
# 最终当板 board 的结果是 [[1,2,3],[4,5,0]] 谜板被解开。
#
# 给出一个谜板的初始状态，返回最少可以通过多少次移动解开谜板，如果不能解开谜板，则返回 -1 。
#
# 示例：
#
#
# 输入：board = [[1,2,3],[4,0,5]]
# 输出：1
# 解释：交换 0 和 5 ，1 步完成
#
#
#
# 输入：board = [[1,2,3],[5,4,0]]
# 输出：-1
# 解释：没有办法完成谜板
#
#
#
# 输入：board = [[4,1,2],[5,0,3]]
# 输出：5
# 解释：
# 最少完成谜板的最少移动次数是 5 ，
# 一种移动路径:
# 尚未移动: [[4,1,2],[5,0,3]]
# 移动 1 次: [[4,1,2],[0,5,3]]
# 移动 2 次: [[0,1,2],[4,5,3]]
# 移动 3 次: [[1,0,2],[4,5,3]]
# 移动 4 次: [[1,2,0],[4,5,3]]
# 移动 5 次: [[1,2,3],[4,5,0]]
#
#
#
# 输入：board = [[3,2,4],[1,5,0]]
# 输出：14
#
#
# 提示：
#
#
# board 是一个如上所述的 2 x 3 的数组.
# board[i][j] 是一个 [0, 1, 2, 3, 4, 5] 的排列.
#
# Related Topics 广度优先搜索


# leetcode submit region begin(Prohibit modification and deletion)
from collections import namedtuple
from heapq import heappush, heappop
from typing import List
import itertools


class Node:

    def __init__(self, state, parent=None, h=0):
        self.state = state
        self.parent = parent
        self.g = parent.g + 1 if parent else 0
        self.h = h
        self.f = self.g + self.h
        self.zero = state.index(0)

    def __lt__(self, other):
        return self.f < other.f


class Solution:
    def slidingPuzzleBiAStar(self, board: List[List[int]]) -> int:
        R, C = len(board), len(board[0])
        start = tuple(itertools.chain(*board))
        n = R * C
        goal_pos = {(C * r + c + 1) % (R * C): (r, c) for r in range(R) for c in range(C)}
        start_pos = {start[C * r + c]: (r, c) for r in range(R) for c in range(C)}

        target = tuple((i + 1) % n for i in range(n))

        def heuristic(start, target_pos):
            res = 0
            for r in range(R):
                for c in range(C):
                    val = start[c + r * C]
                    if val == 0: continue
                    res += abs(r - target_pos[val][0]) + abs(c - target_pos[val][1])
            return res

        bq, eq, rev = [Node(start, h=0)], [
            Node(target, h=0)], False
        b_scores = {start: bq[0]}
        e_scores = {target: eq[0]}
        count = 0
        while bq:
            size = len(bq)
            while size:
                size -= 1
                node = heappop(bq)
                count += 1
                f, g, board, zero = node.f, node.g, node.state, node.zero
                if b_scores[board].f < node.f: continue
                if board in e_scores:
                    return node.g + e_scores.get(board).g
                for nei in [nei for nei in [1 + zero, -1 + zero, C + zero, -C + zero] if
                            abs(nei // C - zero // C) + abs(nei % C - zero % C) == 1 and 0 <= nei < n]:
                    new_board = list(board)
                    new_board[nei], new_board[zero] = new_board[zero], new_board[nei]
                    new_board = tuple(new_board)
                    nn = Node(new_board, node, heuristic(new_board, goal_pos))
                    if nn.f < b_scores.get(new_board, Node(new_board, h=float('inf'))).f:
                        heappush(bq, nn)
                        b_scores[new_board] = nn
            if len(bq) > len(eq):
                bq, eq, b_scores, e_scores, goal_pos, start_pos, rev = eq, bq, e_scores, b_scores, start_pos, goal_pos, not rev
        return -1

    def slidingPuzzle(self, board):
        R, C = len(board), len(board[0])
        expected = {(C * r + c + 1) % (R * C): (r, c) for r in range(R) for c in range(C)}
        start = tuple(itertools.chain(*board))
        target = tuple(list(range(1, R * C)) + [0])
        Node = namedtuple('Node', ['heuristic_score', 'distance', 'board', 'zero'])
        heap = [Node(0, 0, start, start.index(0))]
        scores = {start: 0}

        def heuristic(board):
            res = 0
            for i in range(R):
                for j in range(C):
                    val = board[i * C + j]
                    if val == 0: continue
                    res += abs(expected[val][0] - i) + abs(expected[val][1] - j)
            return res

        while heap:
            node = heappop(heap)
            if node.board == target: return node.distance
            if scores[node.board] < node.heuristic_score: continue
            zero = node.zero

            for d in (-1, 1, -C, C):
                nei = zero + d
                # 如果只移动了一格
                if abs(zero // C - nei // C) + abs(zero % C - nei % C) != 1:
                    continue
                if 0 <= nei < R * C:
                    new_board = list(node.board)
                    new_board[nei], new_board[zero] = new_board[zero], new_board[nei]
                    new_board = tuple(new_board)
                    ng = node.distance + 1
                    nf = heuristic(new_board) + ng
                    if nf < scores.get(new_board, float("inf")):
                        heappush(heap, Node(nf, ng, new_board, nei))
                        scores[new_board] = nf

        return -1


# leetcode submit region end(Prohibit modification and deletion)
print(Solution().slidingPuzzle([[3, 2, 4], [1, 5, 0]]))
