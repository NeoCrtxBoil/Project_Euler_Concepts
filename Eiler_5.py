# https://projecteuler.net/problem=5



import math



def Eiler_5(biggest_div :int):
	result = 1
	if biggest_div > 1:
		result = 2 ** int_log(biggest_div, 2)
		primal_divs = [2]
	for c in range(3, biggest_div + 1, 2):
		if not_primal(c, primal_divs):
			continue
		result *= c ** int_log(biggest_div, c)
	return result



def int_log(x :float, base :float):
	return math.floor(math.log(x, base))



def not_primal(n :int, primal_divs):
	stop = math.floor(math.sqrt(n))
	for c in primal_divs:
		if c > stop:
			break
		if n % c == 0:
			return True
	primal_divs.append(n)
	return False



if __name__ == "__main__":
	print(Eiler_5(20))
