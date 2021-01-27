# !/usr/bin/env python
# -*-coding:utf-8-*-
# @Time    : 2021/1/26 9:30
# @Author  : xiaoxia
# @File    : 大整数运算.py


def add(a, b):
	"""
	高精度加法
	:param a:
	:param b:
	:return:
	"""
	t = 0
	c = []
	for i in range(max(len(a), len(b))):
		if i >= len(a):
			c.append(b[i] + t)
			t = 0
		elif i >= len(b):
			c.append(a[i] + t)
			t = 0
		else:
			d = a[i] + b[i]
			c.append((d + t) % 10)
			t = (d + t) // 10
	if t > 0:
		c.append(t)
	return ''.join(map(str, c[::-1]))


def sub(a, b):
	"""
	高精度减法
	:param a:
	:param b:
	:return:
	"""
	flag = True
	if len(a) < len(b):
		flag = False
	elif len(a) == len(b) and a[-1] < b[-1]:
		flag = False
	c = []
	if flag:
		for i in range(len(a)):
			if i >= len(b):
				if a[i] < 0:
					a[i+1] -= 1
					c.append(10+a[i])
				else:
					c.append(a[i])
			elif a[i] >= b[i]:
				c.append(a[i]-b[i])
			else:
				c.append(a[i]-b[i]+10)
				a[i+1] -= 1
		while c[-1] == 0 and len(c) > 1:
			c.pop()
		return ''.join(map(str, c[::-1]))
	else:
		for i in range(len(b)):
			if i >= len(a):
				if b[i] < 0:
					b[i+1] -= 1
					c.append(10 + b[i])
				else:
					c.append(b[i])
			elif b[i] >= a[i]:
				c.append(b[i]-a[i])
			else:
				c.append(b[i]-a[i]+10)
				b[i+1] -= 1
		while c[-1] == 0 and len(c) > 1:
			c.pop()
		return '-' + ''.join(map(str, c[::-1]))


def mul_one(a, b):
	"""
	高精度乘法，b为普通数
	:param a:
	:param b:
	:return:
	"""
	t = 0
	c = []
	for i in range(len(a)):
		d = a[i] * b
		c.append((d + t) % 10)
		t = (d + t) // 10
	if t > 0:
		c.append(t)
	return c


def mul(a, b):
	"""
	高精度乘法
	:param a:
	:param b:
	:return:
	"""
	c = [0]
	for i in range(len(b)):
		e = mul_one(a, b[i])
		for t in range(i):
			e.insert(0, 0)
		# 真正写的时候不需要这么麻烦，直接让add函数返回需要的数组即可
		c = list(map(int, list(add(c, e))[::-1]))
	return ''.join(map(str, c[::-1]))


def div_one(a, b):
	"""
	高精度除法，b为普通数
	:param a:
	:param b:
	:return:
	"""
	c = []
	s = 0
	for i in range(len(a)-1, -1, -1):
		s = s*10+a[i]
		if s >= b:
			c.append(s // b)
			s = s % b
		else:
			c.append(0)
	while c[0] == 0 and len(c) > 1:
		c.pop(0)
	return ''.join(map(str, c)), s


if __name__ == '__main__':
	a = list(map(int, list(input()[::-1])))
	b = int(input())
	print(div_one(a, b))
