'''
https://www.hackerrank.com/contests/projecteuler/challenges/euler001/problem

Calculate the sum of all multiples of 3 and 5 less than a given integer n.

This seems trivial. My first attempt was one line:
    return sum(set(list(range(0, n, 3)) + list(range(0, n, 5))))

This passes most of the unit tests, but fails tests 2 and 3 with "runtime error"
I'm frustrated that we aren't given more info. The full specs do say 1 <= n <= 10^9.

Testing n that large essentially crashes my computer.

My next attempt will be to use the sum of consecutive integers formula.
I expect that f(15) + f(30) + f(45) + ... + f(15m)  will equal k + 2k + 3k + ... + mk,
so we can use (n(n+1)/2) with our input // 15 and just calculate the remainder.

----

Right direction, but that was half cocked. The right formula will be:
m = n // 15
(f(15) * m) + (105 * ((m - 1) * m)/2)) + sum of valid integers between 15m and n. 

Each group of 15 has seven valid ints in it (0, 3, 5, 6, 9, 10, 12).
Therefore each segment will add (m - 1) * 7 * 15, plus the sum of those 7 numbers (45)

e.g. 0-14 =   0 + 45
    15-29 = 105 + 45
    30-44 = 210 + 45

So, when n = 45, m = 3, and we can find this segment by calculating 
(0 + 1 + 2) * 105 + 3 * 45

Then we can manually add up to 6 valid integers from the last segment.


===

Having completed it, there's a simpler way:

Sum of multiples of 3, plus the sum of the multiples of 5, minus 
 multiples of 15.

'''



def sum_35(n):
    ''' Return the sum of all multiples of 3 and 5 less than n '''
    m = n // 15
    total = (45 * m) + (105 * ((m - 1) * m) // 2)

    for i in range(m * 15, n):
        if i % 3 == 0 or i % 5 == 0:
            total += i

    return total

def sum_35_better(n):
   ''' From the editorial answer: sum of 3s + sum of 5s - sum of 15s '''
   def s(m): return (m * (m + 1)) // 2

   n -= 1      # We're only working with values < n
   return (3 * s(n // 3)) + (5 * s(n // 5)) - ( 15 * s(n // 15))


def sum_35_bf(n):
    ''' old brute force version, kept for testing purposes '''
    return sum(set(list(range(0, n, 3)) + list(range(0, n, 5))))

 
def test_compare_new_to_brute_force():
   for i in range (1000):
      assert sum_35(i) == sum_35_bf(i)


def test_compare_better_to_old():
   for i in range (1000):
      assert sum_35_better(i) == sum_35(i)

      
def main():
   pass


if __name__ == '__main__':
    main()
