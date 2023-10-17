# https://projecteuler.net/problem=6

def Eiler_6(m :int):
	total = (m * (1 + m) // 2) ** 2
	for c in range(1, m + 1):
		total -= c ** 2
	return total

if __name__ == "__main__":
	print(Eiler_6(100))
