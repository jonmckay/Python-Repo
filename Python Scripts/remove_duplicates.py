'''
Created on Apr 18, 2017

@author: jmckay
'''
def remove_duplicates(numbers):
    new_numbers = []
    for i in numbers:
        if i not in new_numbers:
            new_numbers.append(i)
    return new_numbers

print remove_duplicates([1,1,2,2])
            
