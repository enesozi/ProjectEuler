import sys

def main(arg):
    n = int(arg)
    a = calcSquareOfSum(n)
    b = calcSumOfSquares(n)
    print(a-b)

def calcSquareOfSum(n):
    return pow(n*(n+1)//2,2)

def calcSumOfSquares(n):
    return n*(n+1)*(2*n+1)//6

if __name__ == "__main__":
   main(sys.argv[1])
