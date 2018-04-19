import numpy as np
from time import time

def main():
	max_num = 1000000
	# By using memoization, we can boost the execution
	coll_seq = np.zeros(max_num)
	long_seq = 1
	num_for_long_seq = 1
	coll_seq[1] = 1
	for num in range(2,max_num):
		seq = 1
		temp_num = num
		while temp_num > 1:
			if temp_num % 2 == 0:
				temp_num = temp_num // 2
			else:
				temp_num = 3 * temp_num + 1 	
			
			if temp_num < max_num and coll_seq[temp_num] != 0:
				seq = coll_seq[temp_num] + seq
				temp_num = 1		
			else:
				seq = seq + 1

			if seq > long_seq:
				long_seq = seq
				num_for_long_seq = num

		coll_seq[num] = seq			

	print(num_for_long_seq)				

if __name__ == "__main__":
	start_time = time()
	main()
	print("--- %s seconds ---" % (time() - start_time))
