import sys

def main(arg):
   maxNumber = int(arg)
   result = sum([number for number in range(maxNumber) if is_decimal_palindrome(number) and is_binary_palindrome(number)])
   print(result)

def is_decimal_palindrome(number):
	number_to_str = str(number)
	return number_to_str == number_to_str[::-1]   

def is_binary_palindrome(number):
	number_to_bin = bin(number)[2:]
	return number_to_bin == number_to_bin[::-1]

if __name__ == "__main__":
   main(sys.argv[1])
