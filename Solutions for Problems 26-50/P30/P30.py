import sys

def main(arg):
	n_th_pow = int(arg)
	max_num = pow(9,n_th_pow)*n_th_pow
	result = 0
	for num in range(2,max_num+1):
		pow_sum = sum([pow(int(digit),n_th_pow) for digit in str(num)])
		if pow_sum == num:
			result = result + num

	print(result)
			
if __name__ == "__main__":
	main(sys.argv[1])
