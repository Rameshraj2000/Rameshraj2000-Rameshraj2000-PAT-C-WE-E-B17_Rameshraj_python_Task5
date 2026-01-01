# people = [
#     {"name": "Alice", "age": 25},
#     {"name": "Bob", "age": 17},
#     {"name": "Charlie", "age": 19},
#     {"name": "David", "age": 16},
#     {"name": "Eve", "age": 22}
# ]
#
# # Step 1: Filter people who are 18 or older using lambda
# # filter() keeps items where the lambda returns True
# adults = list(filter(lambda person: person["age"] >= 18, people))
#
# # Step 2: Map to get only the names of adults
# # map() applies lambda to each item, extracting the name
# adult_names = list(map(lambda person: person["name"], adults))
#
# # Or you can do it in one line (but separate steps are clearer for beginners):
# # adult_names = list(map(lambda p: p["name"], filter(lambda p: p["age"] >= 18, people)))
#
# print("Adults (18+):", adults)
# print("Adult names:", adult_names)

from functools import reduce

# # Task 2: Calculate product of all numbers
#
# # Sample list of numbers
# numbers = [4,11,15,20]
#
# # Using reduce with lambda to calculate product
# # reduce() applies the lambda cumulatively to items
# # x accumulates the result, y is the next value
# product = reduce(lambda x, y: x * y, numbers)
#
# print("Numbers:", numbers)
# print("Product:", product)

# nums = [1, 2, 3, 4, 5, 6]
#
# is_even = lambda x: x % 2 == 0
#
# even_numbers = [n for n in nums if is_even(n)]
# result = [n * n for n in nums if is_even(n)]
#
# print(f"Numbers: {nums}")
# print(f"Even numbers: {even_numbers}")
# print(f"Squares of even numbers: {result}")

# # Simple lambda that checks basic cases
# check_num = lambda s: s.isdigit() or (s[0] == '-' and s[1:].isdigit())
#
# # Test
# print(f"'abc' is number: {check_num('abc')}")
# print(f"'123' is number: {check_num('123')}")
# print(f"'-45' is number: {check_num('-45')}")
#
# from datetime import datetime
#
# # Create a datetime object
# current_date = datetime.now()
#
# # Lambda function to extract year, month, and day
# get_date_parts = lambda d: (d.year, d.month, d.day)
#
# # Call the lambda function
# year, month, day = get_date_parts(current_date)
#
# print("Date:", current_date)
# print("Year:", year)
# print("Month:", month)
# print("Day:", day)

# Function to generate Fibonacci series
def fibonacci(n):
    series = []
    a, b = 0, 1
    for i in range(n):
        series.append(a)
        a, b = b, a + b
    return series

# Lambda function to call Fibonacci function
fib_lambda = lambda n: fibonacci(n)

# Input
n = 7

print("Fibonacci series:")
print(fib_lambda(n))
