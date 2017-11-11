import numpy as np

MAX_SIZE = 32
MAX = 4*np.power(10,6)
fibs = np.ones(MAX_SIZE)
fibs[1] = 2
evenSums = 2

for i in range(1,MAX_SIZE):
    sum = fibs[i] + fibs[i-1]
    if(sum >= MAX):
        break
    if(sum % 2 == 0):
        evenSums += sum
    fibs[i+1] = sum

print(int(evenSums))
