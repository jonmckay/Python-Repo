'''
Created on Apr 18, 2017

@author: jmckay
'''
def censor(text, word):
    text = text.split()
    new_text = []
    for i in text:
        if i == word:
            new_text.append("*" * len(word))
        else:
            new_text.append(i) 
    return " ".join(new_text)

print censor('this test is a test test', 'this')