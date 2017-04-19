'''
Created on Apr 18, 2017

@author: jmckay
'''
def purify(numbers):
    new_numbers = []
    for i in numbers:
        if i % 2 == 0:
            new_numbers.append(i)
    return new_numbers

print purify([1,2,3])