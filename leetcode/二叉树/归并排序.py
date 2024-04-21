#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/4/21 14:24
# @Author  : xuxiaojun
# @File    : 归并排序.py
# @Description :

# 题目链接
# https://mp.weixin.qq.com/s/7_jsikVCARPFrJ6Hj1EYsg


# 1 4  2 5
# 1 4  2 5
# 1 2 4 5

# 1 4  2 3
# 1 4  2 3
# 1 2  4 3
class Solution:
    @staticmethod
    def _merge(num_list, left_, right_, mid_):
        list_new = []
        right_index = mid_ + 1
        left_index = left_
        while left_index <= mid_ or right_index <= right_:
            try:
                if right_index > right_:
                    list_new.append(num_list[left_index])
                    left_index += 1
                    continue
                if left_index > mid_:
                    list_new.append(num_list[right_index])
                    right_index += 1
                if num_list[left_index] > num_list[right_index]:
                    list_new.append(num_list[right_index])
                    right_index += 1
                    continue
                else:
                    list_new.append(num_list[left_index])
                    left_index += 1
            except Exception as e:
                print(e)
                print(right_index, right_)

        list_new_index = 0
        for index_ in range(left_, right_ + 1):
            a = list_new[list_new_index]

            num_list[index_] = list_new[list_new_index]
            b = num_list[index_]
            list_new_index += 1

    def _sort_fun(self, num_list, left_, right_):
        if left_ >= right_:
            return
        mid_ = (left_ + right_) // 2
        self._sort_fun(num_list, left_, mid_)
        self._sort_fun(num_list, mid_ + 1, right_)
        self._merge(num_list, left_, right_, mid_)

    def sort_fun(self, num_list):
        """
        归并排序
        :param num_list:
        :return:
        """
        self._sort_fun(num_list, 0, len(num_list) - 1)


if __name__ == '__main__':
    input_num_list = [1, 7, 3, 2, 8, 4, 0, 6]
    Solution().sort_fun(input_num_list)
    print(input_num_list)
