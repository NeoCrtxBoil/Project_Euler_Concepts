# https://projecteuler.net/problem=6

def Eiler_6(m :int):
#	result = (m * (1 + m) // 2) ** 2		# (1 + 2 + ... + m)^2		squared sum of 1-st m terms of arithmetic progression (a1 = 1 ; d = 1)
#	result -= m * (m + 1) * (2 * m + 1) // 6	# (1^2 + 2^2 + ... + m^2)	Formula of the sum of squares of the first m numbers
	result = int(m * (m * m - 1) * (m + 2 / 3) // 4)
	return result

if __name__ == "__main__":
	print(Eiler_6(100))
