# -*- coding: utf-8 -*-

height = 1.75
weight = 80.5

bmi = weight / height*height;

if bmi < 18.5:
	print('%f <18.5' % bmi)
elif 25 > bmi >= 18.5:
	print('%f 18.5 - 25' % bmi)
else:
	print('%f >=28' % bmi)