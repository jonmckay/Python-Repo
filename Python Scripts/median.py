'''
Created on Apr 18, 2017

@author: jmckay
'''
def median(numbers):
    numbers.sort()
    halfway = (len(numbers)) / 2
    print halfway
    if len(numbers) % 2 == 0:
        med = (numbers[halfway - 1] + numbers[halfway]) / (2.0)
    else:
        med = numbers[halfway]
    
    return med

print median([5,1,4,3,7,8,9])
    