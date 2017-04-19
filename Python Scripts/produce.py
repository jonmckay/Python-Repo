'''
Created on Apr 18, 2017

@author: jmckay
'''
def product(numbers):
    number_size = len(numbers)
    product = 1
    while number_size > 0:
        product *= numbers[number_size-1]
        number_size -= 1
    
    return product

print product([4, 5, 5])