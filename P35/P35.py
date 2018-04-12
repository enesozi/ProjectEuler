from math import sqrt,floor
import numpy as np
import sys

def main(arg):
   maxNumber = int(arg)
   primeList = sieve(maxNumber)
   result = sum([1 for prime in primeList if is_circular(prime)])
   print(result-1)

def sieve(n):
	primes = np.full(n,True,dtype=bool)
	primes[0] = False 
	primes[1] = False
	for i in range(2,floor(sqrt(n))+1):
		if(primes[i]):
			for j in range(i*i,n,i):
				primes[j] = False

	return np.where(primes)[0]

def is_prime(number):
	maxRange = floor(sqrt(number))
	for i in range(2,maxRange):
		if(number % i == 0):
			return False
	return True		

def is_circular(number):
    number_str = str(number)
    iterations = len(number_str) - 1

    for _ in range(iterations):
        number_str = number_str[-1]+number_str[:-1]
        if not is_prime(int(number_str)):
            return False
    return True           

if __name__ == "__main__":
   main(sys.argv[1])
