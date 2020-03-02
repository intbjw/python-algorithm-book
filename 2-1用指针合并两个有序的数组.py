#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/3/2 15:34
# @Author : Moewww
# @File : 2-1用指针合并两个有序的数组.py
# @Software: PyCharm

arr1 = [1, 3, 4, 6, 10]
arr2 = [2, 5, 8, 11]
ind = 0
ans = arr1.copy()
for i in range(0,len(arr2)):
    while ind < len(arr1):
        if arr2[i] < arr1[ind]:
            ans.insert(ind + i, arr2[i])
            break
        else:
            ind += 1
else:
    ans = ans + arr2[i:]
print(f'{ans}')