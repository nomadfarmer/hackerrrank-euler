#!/usr/bin/env python3
"""
Hacker Rank Euler+ #002: Even Fibonacci Numbers
https://www.hackerrank.com/contests/projecteuler/challenges/euler002

Return the sum of all even numbers in the fibonacci sequence up to a given integer.

e.g. f(8) == 10, since {2, 8} is the set of all even numbers in the fibonacci
sequence up to 8.

=================

"""

def binet(n):
    sq5 = 5 ** 0.5
    return round((1 / sq5) * ((((1 + sq5) / 2) ** n) - (((1 - sq5) / 2) ** n)))


def main():
    i = 3
    while True:
        fibi = binet(i)
        if fibi > 4 * 10 ** 16:
            break
        print (i, fibi)

        
if __name__ == '__main__':
    main()
    
