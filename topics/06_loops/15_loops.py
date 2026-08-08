"""Simple examples of using loops in Python."""

def count_up(n):
	"""Count from 1 to n using a for-loop."""
	for i in range(1, n + 1):
		print(i)


def find_even(numbers):
	"""Yield even numbers from the given iterable using a while-loop."""
	i = 0
	evens = []
	while i < len(numbers):
		if numbers[i] % 2 == 0:
			evens.append(numbers[i])
		i += 1
	return evens


def main():
	print('Counting up to 5:')
	count_up(5)

	nums = [1, 2, 3, 4, 5, 6]
	print('\nEven numbers in', nums, ':', find_even(nums))

# Run the main function if this script is executed directly
if __name__ == '__main__':
	main()

