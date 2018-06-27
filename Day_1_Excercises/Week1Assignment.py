# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 17:13:44 2018

@author: alexrazer
"""
#%%
#Prints out the numbers from 1 to 100 with multiples of 3 as Fizz, multiples of 5 as buzz and of both as fizzbuzz
for n in range(101):
    if n%3 == 0 and n%5 == 0:
        print("FizzBuzz")
    elif n%3 == 0:
        print("Fizz")
    elif n%5 == 0:
        print("Buzz")
    else:
        print(n)
 
#%%
num_dict = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),
           (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
           
def Integer_to_Roman(num):
    roman = ''

    while num > 0:
        for i, r in num_dict:
            while num >= i:
                roman += r
                num -= i

    return roman


print(Integer_to_Roman(3))



#%%

letter = ['a','b','c', 'd','e', 'f', 'g',
               'h','i', 'j', 'k', 'l', 'm', 'n',
                 'o', 'p', 'q','r', 's', 't', 'u',
                 'v','w','x', 'y', 'z']
                 

                


def ROT13(strng):
    new = ""
    
    for i in strng:
        temp = letter.index(i)
        temp += 13
        temp = temp%26
        new += letter[temp]
        
    return new
    
print(ROT13("abcd"))