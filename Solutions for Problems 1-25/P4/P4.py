import sys

def main(arg):
    length = int(arg)
    palNumber = 0
    maxNumber,minNumber = generateMaxNumberWithLength(length)
    for i in range(minNumber,maxNumber+1):
        for j in range(minNumber,maxNumber+1):
            prod = i*j;
            if(isPalindrome(prod)):
                if(palNumber < prod):
                    palNumber = prod

    print(palNumber)


def generateMaxNumberWithLength(length):
    maxNum=0
    minNum = pow(10,length-1)
    for i in range(0,length):
        maxNum += 9*pow(10,i)
    return maxNum,minNum

def isPalindrome(prod):
    s = str(prod)
    l = len(s)
    for i in range(l//2):
        if(s[i] != s[l-1-i]):
            return False
    return True

if __name__ == "__main__":
   main(sys.argv[1])
