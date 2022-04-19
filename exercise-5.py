# exercise-05 Fibonacci sequence for first 50 terms

# Write the code that:
# 1. Calculates and prints the first 50 terms of the fibonacci sequence.
# 2. Print each term and number as follows:
#      term: 0 / number: 0
#      term: 1 / number: 1
#      term: 2 / number: 1
#      term: 3 / number: 2
#      term: 4 / number: 3
#      term: 5 / number: 5
#      etc.

# Hint: The next number is found by adding the two numbers before it

num1 = 0
num2 = 1
for x in range(0, 50):
    print(f'term: {x} / number: {num1}')
    next = num1 + num2
    num1 = num2
    num2 = next

# very slow after the first 30 terms:
# def fibonacci (num):
#     if num < 0: return
#     if num == 0 or num == 1: answer = num
#     else:
#         return fibonacci(num - 1) + fibonacci(num - 2)

# for i in range(50):
#     print(f'term: {i} / number: {fibonacci(i)}')