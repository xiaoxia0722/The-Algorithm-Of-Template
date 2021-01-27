# !/usr/bin/env python
# -*-coding:utf-8-*-
# @Time    : 2021/1/27 9:55
# @Author  : xiaoxia
# @File    : 前缀和差分.py

"""
前缀和: Si = a1+a2+...+ai
前缀和主要用于求某一区间内的和
"""
N = 1002


def prefix_one(a, l, r):
	"""
	一维
	:param a:
	:param l:
	:param r:
	:return:
	"""
	s = [a[0]]
	for i in range(1, len(a)):
		s.append(s[i-1] + a[i])
	if l == 0:
		return s[r]
	return s[r] - s[l-1]


def prefix_two(a, x1, y1, x2, y2):
	s = [[0 for _ in range(N)] for i in range(N)]
	s[0][0] = a[0][0]
	for i in range(len(a)):
		for j in range(len(a[0])):
			if i == 0 and j != 0:
				s[i][j] = s[i][j-1] + a[i][j]
			elif i != 0 and j == 0:
				s[i][j] = s[i-1][j] + a[i][j]

			elif i != 0 and j != 0:
				s[i][j] = s[i-1][j] + s[i][j-1] - s[i-1][j-1] + a[i][j]
	return s[x2][y2] - s[x2][y1-1] - s[x1-1][y2] + s[x1-1][y1-1]


if __name__ == '__main__':
    a = [[1, 2, 3, 4],
         [1, 2, 3, 4],
         [4, 5, 6, 7],
         [4, 3, 5, 2]]
    print(prefix_two(a, 1, 1, 3, 3))

