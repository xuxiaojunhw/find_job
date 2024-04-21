#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/4/21 20:03
# @Author  : xuxiaojun
# @File    : 寻找第k小的元素.py
# @Description :

# https://leetcode.cn/problems/kth-smallest-element-in-a-bst/description/

# 给定一个二叉搜索树的根节点 root ，和一个整数 k ，请你设计一个算法查找其中第k 个最小元素（从1开始计数）。

# 示例1
# 输入：root = [3, 1, 4, null, 2], k = 1
# 输出：1

# 示例 2：
# 输入：root = [5, 3, 6, 2, 4, null, null, 1], k = 3
# 输出：3


# 提示：
# 树中的节点数为n 。
# 1 <= k <= n <= 104
# 0 <= Node.val <= 104

# 进阶：如果二叉搜索树经常被修改（插入 / 删除操作）并且你需要频繁地查找第 k 小的值，你将如何优化算法？


class TreeNode:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right


class Solution(object):
    def __init__(self):
        self.k = None
        self.res_value = None
        self.index = 0

    def _kth_smallest(self, node: TreeNode):
        """
        低效的解法
        :param node:
        :return:
        """
        if not node:
            return
        self._kth_smallest(node.left)
        self.index += 1
        if self.index == self.k:
            self.res_value = node.value
            return
        self._kth_smallest(node.right)



    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.k = k
        self._kth_smallest(root)
        return self.res_value

    def deserialize(self, input_list):
        root_node = TreeNode(input_list[0], None, None)
        node_queue = [root_node]
        index_ = 1
        while index_ < len(input_list):
            node = node_queue.pop(0)
            left_value = input_list[index_]
            if not left_value:
                node.left = None
            else:
                node.left = TreeNode(left_value, None, None)
                node_queue.append(node.left)
            index_ += 1
            right_value = input_list[index_]
            if not right_value:
                node.right = None
            else:
                node.right = TreeNode(right_value, None, None)
                node_queue.append(node.right)
            index_ += 1
        return root_node


if __name__ == '__main__':
    input_list_ = [3, 1, 4, None, 2]
    root_node = Solution().deserialize(input_list_)
    res = Solution().kthSmallest(root_node, 4)
    print(res)
