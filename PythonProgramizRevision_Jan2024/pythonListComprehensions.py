# Find out the square of each number in the list
numbers = [1, 2, 3, 4, 5]
sqr_nums = [i ** 2 for i in numbers]
print(sqr_nums)  # [1, 4, 9, 16, 25]

# filtering even numbers from 1 to 100
even_num = [i for i in range(1, 100) if (i % 2) == 0]
print(even_num)

# find even numbers that are divisible by 5
num_list = [y for y in range(100) if y % 2 == 0 if y % 5 == 0]
print(num_list)

# find vowel in the string "Python"
word = "Python"
vowels = "aeiou"
result = [i for i in word if i in vowels]
print(result)

multiplication = [[i * j for j in range(1, 6)] for i in range(2, 5)]
print(multiplication)  # [[2, 4, 6, 8, 10], [3, 6, 9, 12, 15], [4, 8, 12, 16, 20]]

