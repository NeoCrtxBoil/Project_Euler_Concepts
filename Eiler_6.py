# https://projecteuler.net/problem=6

def Eiler_6(m :int):
	result = (m * (1 + m) // 2) ** 2
	result -= m * (m + 1) * (2 * m + 1) // 6
	return result

if __name__ == "__main__":
	print(Eiler_6(100))
