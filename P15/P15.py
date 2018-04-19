import sys

def main(args):
	N = int(args[1])
	K = int(args[2])
	print(calc_comb(N+K,min(N,K)))

def calc_comb(N,K):
	numerator = 1
	for i in range(K):
		numerator = numerator * N
		N = N - 1
	denominator = calc_fact(K)
	return numerator // denominator		

def calc_fact(K):
	if K == 1:
		return 1
	return K * calc_fact(K-1)	

if __name__ == "__main__":
	main(sys.argv)