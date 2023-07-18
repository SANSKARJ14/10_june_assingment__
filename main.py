#assingment 8

"""
1. In Python, what is the difference between a built-in function and a user-defined function? Provide an
example of each.

Built-in functions are functions that are pre-defined in the Python language and are readily available for use without
requiring any additional steps for their implementation.

my_list = [1, 2, 3, 4, 5]
length = len(my_list)
print(length)  # Output: 5

functions created by the user or programmer to fulfill specific requirements or to modularize code.
These functions are defined using the keyword def

def square(number):
    return number ** 2

result = square(5)
print(result)  # Output: 25
"""
"""
2. How can you pass arguments to a function in Python? Explain the difference between positional
arguments and keyword arguments.

you can pass arguments to a function in the following ways:

a)Positional Arguments:
Positional arguments are passed to a function based on their position or order.
The values are assigned to the function parameters in the same order they appear.

example 

def add_numbers(x, y):
    sum = x + y
    print("The sum is:", sum)

add_numbers(3, 5)

b) Keyword Arguments:
Keyword arguments allow you to explicitly specify the parameter names when passing arguments to a function.
you use the parameter name followed by the value you want to assign to it.

example

def greet(name, age):
    print("Hello", name)
    print("You are", age, "years old")

greet(name="Bob", age=30)

c)Variable-Length Arguments:
Python also supports variable-length arguments, where you can pass a variable number of arguments to a function.
There are two types of variable-length arguments:

*args: It allows you to pass a variable number of positional arguments to a function.
**kwargs: It allows you to pass a variable number of keyword arguments to a function.
"""
"""
3. What is the purpose of the return statement in a function? Can a function have multiple return
statements? Explain with an example.

The purpose of the return statement in a function is to specify the value that the function should evaluate to and
provide as its output. When a return statement is encountered in a function, it immediately terminates the execution
of the function and returns the specified value or expression.

The return statement serves several purposes:

Output: It allows a function to produce a result or output that can be used in other parts of the program.

Termination: It ends the execution of the function at the point where the return statement is encountered.
Any code after the return statement within the function will not be executed.

Passing Data: It can be used to pass data back from a function to the calling code.

A function can have multiple return statements. When a return statement is encountered, the function immediately exits,
and the specified value is returned.
Therefore, only the code leading up to the first return statement that is executed will have an effect.

example
def absolute_value(num):
    if num >= 0:
        return num
    else:
        return -num

result1 = absolute_value(5)
print(result1)  # Output: 5

result2 = absolute_value(-8)
print(result2)  # Output: 8

"""
"""

4. What are lambda functions in Python? How are they different from regular functions? Provide an
example where a lambda function can be useful.


Lambda functions, also known as anonymous functions, are small, inline functions in Python
that are defined without a name. They are created using the lambda keyword and can take any number of arguments
but can only have a single expression.

Lambda functions are different from regular functions in a few key ways:

Syntax: Lambda functions are defined using the lambda keyword followed by the argument list,
a colon, and the expression to be evaluated. Regular functions are defined using the def keyword,
a function name, parentheses for the argument list, a colon, and a block of code.

Nameless: Lambda functions are anonymous, meaning they do not have a name associated with them.
They are primarily used when a small, one-time function is needed without the need for a formal function definition.

Expression-based: Lambda functions are limited to a single expression and cannot contain multiple statements
or a return statement. They automatically return the result of the expression.

Lambda functions can be useful in situations where a simple, one-line function is required, especially as arguments
to higher-order functions like map(), filter(), or sort().
They are commonly used for short and concise operations without the need for a full function definition.

example 

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, my_list))
print(even_numbers)

"""
"""
5.How does the concept of "scope" apply to functions in Python? Explain the difference between local
scope and global scope.

"scope" refers to the region or context in which a variable or name can be accessed or referenced.
The concept of scope applies to functions in Python and determines the visibility and lifetime of variables within a function.

Local Scope:
Local scope refers to the region within a function where variables are defined and accessible.
Variables defined inside a function have local scope, meaning they can only be accessed within that function.

Example:
def my_function():
    x = 10  # Local variable
    print(x)

my_function()  # Output: 10
print(x)  # Error: NameError: name 'x' is not defined

Global Scope:
Global scope refers to the outermost level of a Python program, outside of any function or class.
Variables defined in the global scope are accessible from any part of the program, including inside functions.

example 

x = 10  # Global variable

def my_function():
    print(x)

my_function()  # Output: 10
print(x)  # Output: 10
"""
"""
6.How can you use the "return" statement in a Python function to return multiple values?

ou can use the return statement in a function to return multiple values by separating them with commas.
The values are typically enclosed within parentheses

def calculate_statistics(numbers):
    minimum = min(numbers)
    maximum = max(numbers)
    average = sum(numbers) / len(numbers)
    return minimum, maximum, average

my_numbers = [10, 5, 15, 8, 12]
min_value, max_value, avg_value = calculate_statistics(my_numbers)

print("Minimum value:", min_value)
print("Maximum value:", max_value)
print("Average value:", avg_value)
"""
"""
7.What is the difference between the "pass by value" and "pass by reference" concepts when it
comes to function arguments in Python?


pass by Value:
In a programming language that strictly follows pass by value, a copy of the value is made and passed to the function.
Any modifications made to the parameter inside the function do not affect the original value outside the function.

Pass by Reference:
In a programming language that strictly follows pass by reference, a reference to the original variable or object
is passed to the function. Modifying the parameter inside the function affects the original value outside the function.

in Python:

Immutable objects (such as numbers, strings, and tuples) are effectively passed by value because 
you cannot change their internal state. Any reassignment or modification inside the function creates a new object, 
which doesn't affect the original object outside the function.

Mutable objects (such as lists, dictionaries, and user-defined objects) are effectively passed by reference
because you can modify their internal state. Changes made to the parameter inside the function persist 
outside the function.
"""
"""
8. Create a function that can intake integer or decimal value and do following operations:
a. Logarithmic function (log x)

import math 
import logging 

logging.basicConfig(level = logging.INFO)

def logarathim_function(x):
    try:
        result = math.log(x)
        logging.info(f"logirithm of {x} is {result}")
        return result
    except ValueError as e:
        logging.error(f"error:{e}")
        return f"Error: {e}"

logarathim_function(6)

b)exponential function

def exponential_function(x):
    try:
        result = math.exp(x)
        logging.info(f"The exponential of {x} is {result}")
        return result
    except OverflowError as e:
        logging.error(f"Error: {e}")
        return f"Error: {e}"

c)power function

def power_function(x):
    try:
        result = 2 ** x
        logging.info(f"The result of 2^{x} is {result}")
        return result
    except OverflowError as e:
        logging.error(f"Error: {e}")
        return f"Error: {e}"

d) square root function

def square_root_function(x):
    try:
        result = math.sqrt(x)
        logging.info(f"The square root of {x} is {result}")
        return result
    except ValueError as e:
        logging.error(f"Error: {e}")
        return f"Error: {e}"
"""

#9. Create a function that takes a full name as an argument and returns first name and last name.

def frist_last_names(full_name):
    name = full_name.split()
    if len(name) > 1 :
        frist_name = name[0]
        last_name = name[-1]
        return frist_name , last_name
    else:
        return full_name

print (frist_last_names("sanskar jain"))
print (frist_last_names("sanskar "))









