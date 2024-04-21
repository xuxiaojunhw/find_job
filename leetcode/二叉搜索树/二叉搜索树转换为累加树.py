#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/4/21 20:48
# @Author  : xuxiaojun
# @File    : 二叉搜索树转换为累加树.py
# @Description :

# https://leetcode.cn/problems/convert-bst-to-greater-tree/description/
# 给出二叉 搜索 树的根节点，该树的节点值各不相同，请你将其转换为累加树（Greater Sum Tree），使每个节点 node 的新值等于原树中大于或等于 node.val 的值之和。
#
# 提醒一下，二叉搜索树满足下列约束条件：
#
#     节点的左子树仅包含键 小于 节点键的节点。
#     节点的右子树仅包含键 大于 节点键的节点。
#     左右子树也必须是二叉搜索树。
# 输入：[4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
# 输出：[30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def __init__(self):
        self.sum_value = 0

    def convert_bst(self, node: TreeNode):
        if not node:
            return
        self.convert_bst(node.right)
        self.sum_value += node.val
        node.val = self.sum_value
        self.convert_bst(node.left)

    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.convert_bst(root)
        return root

    def deserialize(self, input_list):
        root_node = TreeNode(input_list[0], None, None)
        node_queue = [root_node]
        index_ = 1
        while index_ < len(input_list):
            node = node_queue.pop(0)
            left_value = input_list[index_]
            if left_value is None:
                node.left = None
            else:
                node.left = TreeNode(left_value, None, None)
                node_queue.append(node.left)
            index_ += 1
            right_value = input_list[index_]
            if right_value is None:
                node.right = None
            else:
                node.right = TreeNode(right_value, None, None)
                node_queue.append(node.right)
            index_ += 1
        return root_node


if __name__ == '__main__':
    input_list_ = [4, 1, 6, 0, 2, 5, 7, None, None, None, 3, None, None, None, 8]
    root_node = Solution().deserialize(input_list_)
    import copy
    res = Solution().convertBST(copy.deepcopy(root_node))
    print(res.val)
    print(res.left.val)
