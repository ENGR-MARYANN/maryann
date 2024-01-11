                                                        # NAME: ONOCHIE MARYANN EZINNE
                                                        # MATRIC-NO: 21/ENG05/056
                                                        # DEPARTMENT: MECHATRONICS
                                                        # COURSE: MCT 307
# What is a loop?
#  A loop is a control structure that allows you to repeat a block of code multiple times. Also,a loop is a programming structure that allows executing a block of code repeatedly.

# Explain the difference between for and while loop with a code block:

# for while loop
#  while loop we can execute a set of statements as long as a condition is true. Also, A while loop repeats a block of code as long as a certain condition is true.
# for example:
i = 0
while i < 5:
    print(i) # Prints i as long as i is less than 5.
    i += 1
    
# for for loop
# A for loop repeats a block of code a specific number of times. Also, A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
# for example;
for i in range(5):
    print(i)   # Prints i as long as i is less than 5.
    
# How to handle exceptions in Python : Use try-except blocks to catch and handle exceptions gracefully.
# Code block using try-except
try:
    # Code that might raise an exception
    num = int(input("Enter a number: "))
    result = 10 / num
    print("Result:", result)
except ZeroDivisionError:
    # What to do if a ZeroDivisionError occurs
    print("Cannot divide by zero!")
except ValueError:
    # What to do if a ValueError occurs
    print("Please enter a valid number!")
    
# What is a function?
# A function is a reusable piece of code that performs a specific task. Functions can take inputs, known as parameters, and return a result.

# What is string?
# A string in programming is a sequence of characters. 

# What is a dictionary and how do you access values by keys?
# A dictionary in Python is an unordered collection of data values that are used to store data values like a map. 
# To access values, use keys within square brackets or the get() method.

# Dictionary example and accessing values by keys
my_dict = {'name': 'Maryann ', 'age': 18, 'city': 'ABUAD'}

# Accessing values by keys
print(my_dict['name'])  # Output: Maryann
print(my_dict.get('age'))  # Output: 18

# What is list comprehension and give examples
# List comprehension is a concise way to create lists in Python. It allows you to create a new list from an existing iterable (like a list, tuple, etc.) in a single, readable line of code.

#  for example;
# to creates a list of the squares of the numbers 0 through 9:
squares = [i**2 for i in range(10)]
print(squares)  # Outputs: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# a list comprehension that only includes the squares of the even numbers in the range:
even_squares = [i**2 for i in range(10) if i % 2 == 0]
print(even_squares)  # Outputs: [0, 4, 16, 36, 64]