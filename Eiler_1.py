def Euler_1(string_of_divs, limit): 
	divs = new_list_of_divs(string_of_divs)
	total = 0
	for c in divs: 
		total += sum_of(c, limit)
	count_of_divs = len(divs)

	if count_of_divs > 1: 
		for c1 in range(count_of_divs - 1): 
			for c2 in range(c1 + 1, count_of_divs): 
				total -= sum_of(divs[c1] * divs[c2], limit)
	if count_of_divs > 2: 
		for c1 in range(count_of_divs - 2): 
			for c2 in range(c1 + 1, count_of_divs - 1): 
				for c3 in range(c2 + 1, count_of_divs): 
					total -= 2*sum_of(divs[c1] * divs[c2] * divs[c3], limit)
	if count_of_divs > 3: 
		for c1 in range(count_of_divs - 3): 
			for c2 in range(c1 + 1, count_of_divs - 2): 
				for c3 in range(c2 + 1, count_of_divs - 1): 
					for c4 in range(c3 + 1, count_of_divs): 
						total -= 3*sum_of(divs[c1] * divs[c2] * divs[c3] * divs[c4], limit)
	return total


#def del_repeats(count_of_divs, divs, loop_insertion = 0):
#	if count_of_divs - loop_insertion > 1:
#		del_repeats(count_of_divs, divs, loop_insertion + 1)
#	else:
		

def new_list_of_divs(string_of_divs): 
	input_string = string_of_divs + ' '
	result = []
	s_int = ''
	for c in input_string: 
		if '0' <= c <= '9': 
			s_int += c
		else: 
			if s_int != '': 
				result.append(int(s_int))
			s_int = ''
	return result


def sum_of(d, m): #difference, max
	n = m // d #quantity
	if m % d == 0: n -= 1
	return d * (n + 1) * n // 2


print(Euler_1('3, 5', 10))
print(Euler_1('3, 5', 100))
print(Euler_1('3, 5', 1000))
print(Euler_1('3, 5', 10000))
print(Euler_1('3, 5', 100000))
print(Euler_1('3, 5', 1000000))
print(Euler_1('3, 5', 10000000))
print(Euler_1('3, 5', 100000000))
print(Euler_1('3, 5', 20))
print(Euler_1('3, 5', 200))
print(Euler_1('3, 5', 2000))
print(Euler_1('3, 5', 20000))
print(Euler_1('3, 5', 200000))
print(Euler_1('3, 5', 2000000))
print(Euler_1('3, 5', 20000000))
print(Euler_1('3, 5', 200000000))
print(Euler_1('3, 5', 30))
print(Euler_1('3, 5', 300))
print(Euler_1('3, 5', 3000))
print(Euler_1('3, 5', 30000))
print(Euler_1('3, 5', 300000))
print(Euler_1('3, 5', 3000000))
print(Euler_1('3, 5', 30000000))
print(Euler_1('3, 5', 300000000))
print(Euler_1('3, 5', 40))
print(Euler_1('3, 5', 400))
print(Euler_1('3, 5', 4000))
print(Euler_1('3, 5', 40000))
print(Euler_1('3, 5', 400000))
print(Euler_1('3, 5', 4000000))
print(Euler_1('3, 5', 40000000))
print(Euler_1('3, 5', 400000000))
