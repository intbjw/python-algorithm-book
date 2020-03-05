#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/3/5 12:18
# @Author : Moewww
# @File : 2-2用指针实现有序数组的二分查找.py
# @Software: PyCharm
numbers = [1, 3, 5, 6, 7, 8, 13, 14, 15, 17, 18, 24, 30, 43, 56]
search = int(input("请输入要查询的数字："))
head, tail = 0, len(numbers)-1
while tail - head > 1:
    mid = (head + tail) // 2
    if mid == search:
        ans = mid
        break
    if search < numbers[mid]:
        tail = mid
    if search > numbers[mid]:
        head = mid + 1
else:
    if search == numbers[head]:
        ans = head
    else:
        ans = -1
print(ans)

