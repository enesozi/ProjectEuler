import sys
import numpy as np

def main(arg):
	boundry = int(arg)
	ami_nums_flag = np.zeros(boundry)

	for num in range(1,boundry):
		if ami_nums_flag[num] == 0:
			sum_prop = sum_proper_divs(num)
			if sum_prop == num:
				ami_nums_flag[num] = -1
			elif sum_prop >= boundry:
				ami_nums_flag[num] = -1
			else:	
				if ami_nums_flag[sum_prop] == 0:
					sum_prop_conj = sum_proper_divs(sum_prop)
					if sum_prop_conj == num:
						ami_nums_flag[num] = 1
						ami_nums_flag[sum_prop] = 1
					else:
						ami_nums_flag[num] = -1
						ami_nums_flag[sum_prop] = -1

	print(sum(np.where(ami_nums_flag == 1)[0]))					

def sum_proper_divs(n):
	result = 0
	for i in range(1, n//2 + 1):
		if n % i == 0:
			result = result + i
	return result
			
if __name__ == "__main__":
	main(sys.argv[1])
