import sys
from math import floor,sqrt 

def main(arg):
	divisor_number = int(arg)
	num = 1
	triangle_num = 0
	while True:
		triangle_num = num*(num + 1)//2
		div_count = 0
		for i in range(1,floor(sqrt(triangle_num))+1):
			if(div_count >= divisor_number):
				break
			if(triangle_num % i == 0):
				if(triangle_num/i == i):
					div_count = div_count + 1					
				else:
					div_count = div_count + 2

		if(div_count >= divisor_number):
			break

		num = num + 1	

	print(triangle_num)

if __name__ == "__main__":
   main(sys.argv[1])
