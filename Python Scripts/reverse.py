'''
Created on Apr 18, 2017
Step through each index backwards and get the character, adding it to a new string

@author: jmckay
'''

def reverse(text):
    new_text = ""
    text_len = len(text) - 1
    while text_len >= 0: 
        new_text += text[text_len]
        text_len -= 1
    return new_text

print reverse('#Jonathan123')