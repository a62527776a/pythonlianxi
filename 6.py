# # -*- coding: utf-8 -*-

# import math

# a = input('please Enter A number');
# b = input('please Enter B number');
# c = input('please Enter C number');


# def quadratic(a, b, c):
# 	a1 = math.sqrt(b**2 - 4 * a * c);
# 	print(a1);
# 	x1 = -b + a1 / 2 * a
# 	x2 = -b - a1 / 2 * a
# 	return x1,x2;


# quadratic(int(a),int(b),int(c));

# def power(x,n = 2):
# 	s = 1
# 	while n > 0:
# 		n = n - 1;
# 		s = s * x;
# 	print(s);
# power(5)

def calc(*numbers):
	sum = 0;
	for n in numbers:
		sum += n ** 2;
	print(sum);

calc([1,5,4,3]);