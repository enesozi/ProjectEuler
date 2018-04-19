import numpy as np

def main():
    factorials = initFactArray()
    sumOfCuriousNumbers = 0
    for i in range(10,int(np.sum(factorials)+1)):
        factSum = 0
        for j in str(i):
            factSum += factorials[int(j)]
        if(factSum == i):
            sumOfCuriousNumbers += i
    print(sumOfCuriousNumbers)

def initFactArray():
    factorials = np.ones(10)
    for i in range(2,10):
        factorials[i] = i*factorials[i-1]
    return factorials

if __name__ == "__main__":
   main()
