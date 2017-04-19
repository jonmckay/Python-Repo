'''
Created on Apr 18, 2017

@author: jmckay
'''

def count(sequence, item):
    counter = 0
    for i in sequence:
        if item == i:
            counter += 1
    return counter

print count([1,2,1,1], 1)