def main():
    print (sum_35(-30))
    print (sum_35(10000000))




def sum_35(n):
    ''' Return the sum of all multiples of 3 and 5 less than n '''
    return sum(set(list(range(0, n, 3)) + list(range(0, n, 5))))
    

if __name__ == '__main__':
    main()
