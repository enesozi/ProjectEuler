import sys

def main(arg):
	n = int(arg)
	result = fact(n)
	print(sum([int(digit) for digit in str(result)]))

def fact(n):
	if n == 1:
		return 1
	return n*fact(n-1)

				
if __name__ == "__main__":
	main(sys.argv[1])

