https://leetcode.com/problems/kth-largest-element-in-an-array/

Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5
Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
Note: 
You may assume k is always valid, 1 ≤ k ≤ array's length.


1. 可以采用K的最大堆
2. 快速选择
Quick Select的目标是找出第k大元素，所以

* 若切分后的pivot == n - k，则第k大元素为pivot；
* 若切分后的pivot < n-k, 则说明在左分区中, 计算 start..pivot
* 若切分后的pivot > n-k, 则说明在右分区中，计算pivot+1..end。