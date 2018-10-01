#!/usr/bin/env python3
"""
Hacker Rank Euler+ #002: Even Fibonacci Numbers
https://www.hackerrank.com/contests/projecteuler/challenges/euler002

Return the sum of all even numbers in the fibonacci sequence up to a given integer.

e.g. f(8) == 10, since {2, 8} is the set of all even numbers in the fibonacci
sequence up to 8.

=================

Tried using Binet's formula. I did discover that we will only be using the first 81 numbers in the fib sequence, but I believe that we're seeing
rounding issues past somewhere around the 69th number.

Tested -- see the test_binet() function. As I guessed, the binet() function
is perfect until 71, when rounding issues become an issue.

Ah, well. The complexity is low enough that the obvious brute force way is fine.

"""

def binet(n):
    """ Binet's Formula finds the nth number in the fibonacci sequence """
    sq5 = 5 ** 0.5
    return round((1 / sq5) * ((((1 + sq5) / 2) ** n) - (((1 - sq5) / 2) ** n)))


def fibs(n):
    """ Return a list of the fibonacci sequence up to the nth number """
    fiblist = [0, 1, 1]
    for i in range(3, n+1):
        fiblist += [ fiblist[i - 1] + fiblist[i - 2] ]
    return fiblist


def test_binet():
    ''' This code helps me double check my implementation of the binet formula '''
    fiblist = fibs(85)
    for i in range (86):
        bin_i = binet(i)
        print(f"i: {i}, fib: {fiblist[i]}, binet: {bin_i}, d: {fiblist[i] - bin_i}")

        
def sum_to_max(l, m):
    return sum(filter(lambda x: x <= m, l))
               

def main():
    even_fibs = list(filter(lambda x: x % 2 == 0, fibs(81)))
    print(sum_to_max(even_fibs, 100))
    print(sum_to_max(even_fibs, 1000))   

    
if __name__ == '__main__':
    main()
    
