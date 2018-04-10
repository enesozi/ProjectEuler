import sys

def main(arg):
	sum = int(arg)
	for x in range(sum//3):
		for y in range(x+1,sum//2):
			z = sum - x - y
			if(x*x + y*y == z*z):
				print(x*y*z)
				break

if __name__ == "__main__":
   main(sys.argv[1])