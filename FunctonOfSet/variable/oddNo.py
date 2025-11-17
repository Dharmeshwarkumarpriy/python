# Using lambda with filter to get odd numbers from 0 to 10
odd_numbers = list(filter(lambda x: x % 2 != 0, range(11)))

# Print the result
print("Odd numbers from 0 to 10:", odd_numbers)

# Using lambda with filter to get odd numbers from 0 to 10
odd_numbers = list(filter(lambda x: x % 2 == 0, range(11)))

# Print the result
print("Odd numbers from 0 to 10:", odd_numbers)
