import sys
from math import sqrt,floor
import numpy as np


def main(arg):
	arg = int(arg)
	primes = sieve(arg)
	print(sum(primes))

def sieve(n):
	primes = np.full(n,True,dtype=bool)
	primes[0] = False 
	primes[1] = False
	for i in range(2,floor(sqrt(n))+1):
		if(primes[i]):
			for j in range(i*i,n,i):
				primes[j] = False

	return np.where(primes)[0]

if __name__ == "__main__":
   main(sys.argv[1])
