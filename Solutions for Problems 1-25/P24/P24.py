import sys
from math import factorial

def main(arg):
	n_th_perm = int(arg) - 1 
	perm_str = ''
	num_len = 10
	num_list = list(range(num_len))
	
	for i in range(1,num_len):
		fact = factorial(num_len-i)
		mul = n_th_perm // fact
		n_th_perm = n_th_perm % fact
		perm_str = perm_str + str(num_list.pop(mul))
		if n_th_perm == 0:
			break

	for i in range(len(num_list)):
		perm_str = perm_str + str(num_list[i])

	print(perm_str)


if __name__ == "__main__":
	main(sys.argv[1])
