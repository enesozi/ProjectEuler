import sys

def main(arg):
    K = int(arg)
    a = findSumOfMultiplesBelow(3,K)
    b = findSumOfMultiplesBelow(5,K)
    c = findSumOfMultiplesBelow(15,K)
    print(a+b-c)


def findSumOfMultiplesBelow(n,K):
    maxMultiple = (K-1)//n;
    return n*maxMultiple*(maxMultiple+1)//2


if __name__ == "__main__":
   main(sys.argv[1])
