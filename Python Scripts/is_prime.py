'''
Created on Apr 18, 2017

@author: jmckay
'''
def is_prime(x):
    #n from 2 to x - 1 test if x is evenly divisible by n
    if x < 2:
        return False
    if x == 2:
        return True
    for n in range(2, x):
        if x % n == 0:
            return False
    else:
        return True


print is_prime(9)