'''
Created on Apr 18, 2017

@author: jmckay
'''

def anti_vowel(text):
    new_text = ""
    for c in text:
        if c not in "AEIOUaeiou":
            new_text += c
    
    return new_text

print anti_vowel('Jonathan')

             