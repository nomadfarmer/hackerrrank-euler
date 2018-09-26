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
(f(15) * m) + (150 * ((m - 1) * m)/2) + sum of valid integers between 15m and n. 

'''


def sum_35(n):
   ''' Return the sum of all multiples of 3 and 5 less than n '''
   return sum(set(list(range(0, n, 3)) + list(range(0, n, 5))))
   
def sum_con_int(n):
   return (n * (n+1)) // 2


def main():
    k = sum_35(15)
    print (f"k = {k}")
    
    for i in range(20):
        m = sum_35(i * 15)
        o = sum_con_int(i)
        
        print (f"i: {i}, digit sum: {o}, f(15i)/k = {m//k}, f(15i) = {m}" )
    

if __name__ == '__main__':
    main()
