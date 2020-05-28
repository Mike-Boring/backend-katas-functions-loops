#!/usr/bin/env python
"""Implements math functions without using operators,
except for '+' and '-'.
"""

__author__ = "Mike Boring"


def add(x, y):
    """Add two integers."""
    result = x + y
    return result


def multiply(x, y):
    """Multiply x with y using the add() function above."""
    result = 0
    if x == 0 or y == 0:
        return 0
    for _ in range(abs(y)):
        result = add(result, abs(x))
    if x < 0 and y < 0:
        return result
    if x > 0 and y > 0:
        return result
    if x < 0 or y < 0:
        return -result


def power(x, n):
    """Raise x to power n, where n >= 0, using the functions above."""
    print(x, n)
    result = x
    if n == 1:
        return x
    if x == 0 and n > 0:
        return 0
    if x < 0 and n == 0:
        return -1
    if x == 0 and n == 0:
        return 1
    if x > 0 and n == 0:
        return 1
    if x == 1 and n > 0:
        return 1
    for _ in range(1, n):
        result = multiply(abs(result), abs(x))
    if x < 0:
        return -result
    if x > 0:
        return result


print(power(-2, 2))  # Not sure why my unit test is failing for power
print(-2 ** 2)  # when this print to terminal proves the proper value is
# is being generated as they match. I am printing
#  out the paramaters in the test output so they can be
# tested against these print functions.


def factorial(x):
    """Compute the factorial of x, where x > 0, using the functions above."""
    result = x
    if x == 0:
        return 1
    for num in range(x-1, 0, -1):
        result = multiply(result, num)
    return result


def fibonacci(n):
    """Compute the nth term of fibonacci sequence using the functions above."""
    fib_list = [0, 1, 1]
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    for _ in range(2, n):
        fib_list.append(add(fib_list[-1], fib_list[-2]))
    return fib_list[-1]


if __name__ == '__main__':
    # your code to call functions above
    pass
