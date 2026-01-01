# #Task 1 people under 18
people = [
    {"name": "Ramesh", "age": 55},
    {"name": "Raj", "age": 17},
    {"name": "Selvaraju", "age": 11},
    {"name": "Calvin", "age": 15},
    {"name": "Klein", "age": 20}
]

# #Filter people who are 18 or older using lambda
adults = list(filter(lambda person: person["age"] >= 18, people))# filter() keeps items where the lambda returns True
#
# # map() applies lambda to each item, extracting the name
adult_names = list(map(lambda person: person["name"], adults))
#
print("Adults (18+):", adults)
print("Adult names:", adult_names)

# #Task 2 use of reduce functon Calculate product of all numbers
from functools import reduce #It reduces a list to a single value

# #Sample list of numbers
numbers = [4,11,15,20]

# #Using reduce with lambda to calculate product
# #reduce() applies the lambda cumulatively to items
product = reduce(lambda x, y: x * y, numbers) #x accumulates the result, y is the next value

print("Numbers:", numbers)
print("Product:", product)

#Task 3 square of even numbers
# List of integers
nums = [1, 2, 5, 13, 10, 8]

# Lamda function which takes x and checks whether the integer is even
is_even = lambda x: x % 2 == 0

even_numbers = [n for n in nums if is_even(n)] #loops through n in nums if is_even is true
result = [n * n for n in nums if is_even(n)] #filters even numbers from is_even and squares them

print(f"Numbers: {nums}")
print(f"Even numbers: {even_numbers}")
print(f"Squares of even numbers: {result}")

#Task 4 check given string is number
# lambda that checks given string has numbers with +-
is_number = lambda s: s.lstrip('+-').isdigit()

# Sample input data
inputs = [
    "123",
    "-45",
    "+78",
    "0",
    "abc",
    "12a",
    "--5",
    ""
]

# Loops and check each value
for value in inputs:
    print(f"'{value}' is number: {is_number(value)}")

# # Task 5 year month date
# #datetime is an inbuilt python module to extract time date year month
from datetime import datetime
#Create a datetime object gives date and time
current_date = datetime.now()
# Lambda function to extract year, month, and day
get_date = lambda d: (d.year, d.month, d.day)

# Call the lambda function
year, month, day = get_date(current_date) #get_date return tuple python unpacks into variable

print("Date:", current_date)
print("Year:", year)
print("Month:", month)
print("Day:", day)

#Task 6 Fibonacci series
# Function to generate Fibonacci series gets input of n like how many numbers you want
def fibonacci(n):
    series = [] #here it stores the series in a list
    a, b = 0, 1 #fibonacci always start with 0, 1 with a current and b as next
    for i in range(n): #this loop runs n times and adds one num to list for each loop
        series.append(a) #current value of a is added to the list
        a, b = b, a + b #updates value a becomes b, b becomes a+b
    return series

# Lambda function to call Fibonacci function
fib_lambda = lambda n: fibonacci(n) #lambda function takes n call fibonacci to return result

# Input
n = 8

print("Fibonacci series:", fib_lambda(n))
