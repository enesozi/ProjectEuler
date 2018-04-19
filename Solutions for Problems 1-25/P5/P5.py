import sys
from functools import reduce

def main(arg):
    l = int(arg)
    print(reduce(lcm,range(1,l+1)))

def gcd(x,y):
    while(y > 0):
        x,y = y,x%y
    return x

# Utilize the fact that product of 2 numbers
# equals to multiplication of their gcd and lcm
def lcm(x,y):
    return (x*y)//gcd(x,y)

if __name__ == "__main__":
   main(sys.argv[1])
