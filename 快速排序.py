# !/usr/bin/env python
# -*-coding:utf-8-*-
# @Time    : 2021/1/12 15:32
# @Author  : xiaoxia
# @File    : 快速排序.py


def qsort(a, l, r):
	if l >= r:
		return
	i = l
	j = r
	while i < j:
		while a[j] >= a[l] and i < j:
			j -= 1
		while a[i] <= a[l] and i < j:
			i += 1
		if i < j:
			a[i], a[j] = a[j], a[i]
	a[l], a[j] = a[j], a[l]
	qsort(a, l, i - 1)
	qsort(a, i + 1, r)


if __name__ == '__main__':
	# 输入需要排序的数组a
	a = list(map(int, input().split()))
	qsort(a, 0, len(a) - 1)
	print(a)
