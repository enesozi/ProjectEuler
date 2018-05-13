from csv import reader
from math import sqrt,floor

def main():
	with open('p042_words.txt', 'r') as csvfile:
		words = next(reader(csvfile))
	alp_vals = [get_word_value(word) for word in words]
	#word_dict = dict(zip(words, map(get_word_value, words)))
	count = 0
	for val in alp_vals:
		goal = 2 * val
		n = floor(sqrt(goal))
		if n*(n+1) == goal:
			count += 1

	print(count)
	

def get_alp_order(letter):
	return ord(letter.lower()) - ord('a') + 1

def get_word_value(word):
	return sum(map(get_alp_order,word))	

if __name__ == "__main__":
	main()
