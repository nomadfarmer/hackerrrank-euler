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
    """ Binet's Formula finds the nth number in the fibonacci sequence """
    sq5 = 5 ** 0.5
    return round((1 / sq5) * ((((1 + sq5) / 2) ** n) - (((1 - sq5) / 2) ** n)))



def main():
    ''' This code is to help me double check my implementation of the binet formula '''
    i = 0
    while True:
        i += 1
        fibi = binet(i)
        if fibi > 4 * 10 ** 16:
            break
        if fibi % 2 == 0: print (i, fibi)

        
if __name__ == '__main__':
    main()
    
