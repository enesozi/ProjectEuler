import numpy as np

def main():
	max_len = 1000
	f_1 = 1
	f_2 = 1
	index = 2
	while len(str(f_2)) < max_len:
		index = index + 1
		f_2, f_1 = f_1+f_2, f_2

	print(index)	

if __name__ == "__main__":
	main()