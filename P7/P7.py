import sys

def main(arg):
    n = int(arg)
    k = 1
    while(n):
        k+=1
        if(isPrime(k)):
            n-=1
    print(k)


def isPrime(p):
    for f in range(2,p):
        if(p%f == 0):
            return False;
    return True;


if __name__ == "__main__":
   main(sys.argv[1])
