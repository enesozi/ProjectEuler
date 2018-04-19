import sys

def main(arg):
    #600851475143
    n = int(arg)

    maxRange = int(np.sqrt(n))
    maxPrime = 1

    for i in range(2,maxRange):
        if(n % i == 0):
            if(isPrime(i)):
                maxPrime = i

    print(maxPrime)

def isPrime(p):
    for f in range(2,p):
        if(p%f == 0):
            return False;
    return True;

if __name__ == "__main__":
   main(sys.argv[1])
