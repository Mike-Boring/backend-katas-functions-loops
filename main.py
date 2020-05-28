#!/usr/bin/env python
"""Implements math functions without using operators,
except for '+' and '-'.
"""

__author__ = "Mike Boring"
# Had a little help from Daniel Lomelino with my functions affecting the tests on the
# power function comparison with x ** y


def add(x, y):
    """Add two integers."""
    return x + y


def multiply(x, y):
    """Multiply x with y using the add() function above."""
    result = 0
    for _ in range(abs(y)):
        result = add(result, x)
    if y < 0:
        return -result
    return result


def power(x, n):
    """Raise x to power n, where n >= 0, using the functions above."""
    result = 1
    for _ in range(n):
        result = multiply(result, x)
    return result


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
