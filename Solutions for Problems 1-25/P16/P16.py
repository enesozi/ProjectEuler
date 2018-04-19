import sys

def main(args):
	N = int(args[1])
	K = int(args[2])
	print(sum([int(digit) for digit in str(pow(N,K))]))


if __name__ == "__main__":
	main(sys.argv)