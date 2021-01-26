# !/usr/bin/env python
# -*-coding:utf-8-*-
# @Time    : 2021/1/17 14:59
# @Author  : xiaoxia
# @File    : 归并排序.py


def merge_sort(a, l, r):
	if l >= r:
		return
	mid = (l + r) // 2
	merge_sort(a, l, mid)
	merge_sort(a, mid + 1, r)
	i = l
	j = mid + 1
	temp = []
	while i <= mid and j <= r:
		if a[i] <= a[j]:
			temp.append(a[i])
			i += 1
		else:
			temp.append(a[j])
			j += 1
	while i <= mid:
		temp.append(a[i])
		i += 1
	while j <= r:
		temp.append(a[j])
		j += 1
	for t in range(len(temp)):
		a[l + t] = temp[t]


if __name__ == '__main__':
	a = [10, 9, 3, 8, 10, 8, 6, 1]
	merge_sort(a, 0, len(a) - 1)
	print(a)
