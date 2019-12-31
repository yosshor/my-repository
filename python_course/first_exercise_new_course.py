# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 09:48:49 2019

@author: EGLOBAL
"""

def factorial(n):
    if n == 1:
        return n
    return n * factorial(n - 1)

factorial(6)            

#try factorial def with reduce func
def for_red(n, t):
    return  n*t
import functools
import numpy as np

m = np.arange(1,6)

k = functools.reduce(for_red, m)           
print(k)
            

# 1.1.2 exercise
      
def double_letter(n):
    return n * 2
w = 'python'
t = ' we are the champions'
print(''.join(list(map(double_letter, t))))


# 1.1.3 exercise

def four_dividers(num):
    return num % 4 == 0
print(list(filter(four_dividers, range(1,10))))
print(list(filter(four_dividers, range(3))))



# 1.1.4 exercise
def sum_of_digits(num1, num2):
    return num1 + num2
print(functools.reduce(sum_of_digits, [104]))
print(list(filter(four_dividers, range(1,10))))
print(list(map((lambda x, y : x + y), [104],[87])))
print(functools.reduce(lambda x, y : x + y, [104]))




import functools
def function(num, item):
    return num + 1
password = input("Enter Your password (integers only): ")
lst = list(map(int, password))
magic = functools.reduce(function, lst)
result = (lambda x: x % 4 == 0)(magic)
if result:
    print("Correct password!")
else:
    print("Wrong password.")



w = [1, 2,3]
e = [5, 6, 7]
f = [i*j for i in w for j in e]
a = [i*j for i in w for j in e if i % 2 == 0]
print(a)
print(f)


def intersection(list1, list2):
    result = [i for i in list1 if i in list2]
    return list(set(result))

print(intersection([1, 2, 3, 4], [8, 3, 9]))
print(intersection([5, 5, 6, 6, 7, 7], [1, 5, 9, 5, 6]))

#def is_prime(num):
#    result = [False  if num % i == 0 else True for i in range(2, num)] #[[i ,False] if (num % i == 0) break else True for i in range(2,num)]
#    return result

a = [list(map(lambda x: num % i, num)) for i in range(2, 6)]
alist = [1,2,3,4,5]
p = [functools.reduce(lambda x,y: x + y, [1,2,3,4,5])]

num = 11
t = int(num/2)
d = functools.reduce(lambda x,y: x+y,map(lambda x:x+x,filter(lambda x: (x>=3), (1,2,3,4)))) 
w = [True if functools.reduce(lambda x, y : x * y, list(map(lambda x: (num % x),  range(2, t)))) != 0 else False]



# 1.3.2 exercise
def is_prime(num):
    t = int(np.floor(num / 2))
    return [True if functools.reduce(lambda x, y : x * y, list(map(lambda x: (num % x),  range(2, t)))) != 0 else False]
is_prime(42)
is_prime(43)



# 1.3.3 exercise

def is_funny(string):
    for char in string:
        if char != 'h' and char != 'a':
            return False
    return True
print(is_funny("hahahahahaha"))

def is_funny(string):
    return set(True if (char == 'a' or char == 'h')  else False for char in string)

print(is_funny("hhhaaa"))


def n(st):
    return [char for char in st]
print(n("haaahhh"))


#lis = [ 1 , 3, 5, 6, 2, 9] 
#
#print ("The sum of the list elements is : ",end="") 
#print (functools.reduce(lambda a,b : a+b,lis)) 
#
#list(map(lambda num: num % range(2, num / 2), ))
#list(functools.reduce(lambda x: True if x == 0 else False, lis))
#
#def is_funny(string):
#    e = [False for char in string if char != 'h' and char != 'a'  ]
#    return set(e)



#1.3.4 exercise 

password = "sljmai ugrf rfc ambc: lglc dmsp mlc rum"
ord(password)
chr(98)
i = [chr(ord(char) + 2) for char in password ]
print(''.join([chr(ord(char) + 2) for char in password ]))



# coin exercise
def combine_coin(num):
    return [str(i) + '$' for i in range(num)]   
    
    
print(combine_coin(5))


import random
p = lambda:random.choice('7♪♫♣♠♦♥◄☼☽')
[print('|'.join([p(),p(),p()]))]# for i in range(85)]



#1.5.1 exercise
with open('new_text.txt', 'r') as p:
    print(max([(len(line)) for line in p]))
 
with open ('new_text.txt', 'r') as p:
    print(max([line for line in p], key = len))
    
#1.5.2 exercise
   
with open('new_text.txt', 'r') as p:
    print([len(line) for line in p])
with open('new_text.txt', 'r') as p:
    print(sum([len(line) for line in p.read().split('\n')]))
#    print(np.sum([len(line) for line in p]))
#    print(sum([len(line) for line in p.read().split('\n')]))
#    print(functools.reduce(lambda x , y: x + y, [line for line in p]))
with open('new_text.txt', 'r') as p:
    print(sum(list(map(lambda x : x - 1, [len(line)  for line in p]))))

#1.5.3 exercise
#כתבו תוכנית שמדפיסה למסך את השמות הכי קצרים בקובץ, כל שם בשורה נפרדת. להלן הפלט הצפוי:


with open('new_text.txt', 'r') as p:
    print([list(filter(lambda t: t== len(min(t.split())), [line for line in p.read().split('/n')]))])
    print([line for line in p.read().split('\n') if len(line) == len(sorted(p.read().split('\n'),key=len)[0])])
    print([p.read().sort(key=len)])# for line in p])
    print([line for line in p if len(line) == len(min([line for line in p], key = len))])
    print([line for line in p if len(line) == min([line for line in p], key = len)])


#the simple solution is this
with open('new_text.txt', 'r') as p:
    [print(line) for line in p.read().split('\n') if len(line) == 2]
#for complex solution we try this but i need to check why its not workink
with open('new_text.txt', 'r') as p:
    [print(line) for line in p.read().split('\n') if len(line) == len(min([line for line in p.read().split('\n')], key = len))]
    print(min([line for line in p.read().split('\n')], key = len))
    print(len(min([line for line in p.read().split('\n')], key = len)))
    [print(line) for line in p.read().split('\n') if len(line) == len(min([p.readline()], key = len))]

#1.5.4 exercise
#כתבו תוכנית שיוצרת קובץ חדש בשם name_length.txt
# המכיל את האורך של כל שם בקובץ names.txt, לפי הסדר, אחד בכל שורה. להלן הפלט הצפוי:

with open('name_length.txt', 'x') as p:
    p.writelines([str(len(line))+'\n' for line in open('new_text.txt').read().split('\n')])


# 1.5.5 exercise
#    כתבו תוכנית שקולטת מהמשתמש מספר המייצג אורך של שם 
#    ומדפיסה את כל השמות בקובץ names.txt שהם באורך הזה. להלן דוגמת הרצה ופלט:

r = int(input('Enter name length :'))
with open('new_text.txt', 'r') as p:
    print('\n'.join([line for line in p.read().split('\n') if len(line) == r]))



from sklearn.linear_model import LogisticRegression
from sklearn.metrics import log_loss
import numpy as np

x = np.array([-2.2, -1.4, -.8, .2, .4, .8, 1.2, 2.2, 2.9, 4.6])
y = np.array([0.0, 0.0, 1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0])

logr = LogisticRegression(solver='lbfgs')
logr.fit(x.reshape(-1, 1), y)

y_pred = logr.predict_proba(x.reshape(-1, 1))[:, 1].ravel()
loss = log_loss(y, y_pred)

print('x = {}'.format(x))
print('y = {}'.format(y))
print('p(y) = {}'.format(np.round(y_pred, 2)))
print('Log Loss / Cross Entropy = {:.4f}'.format(loss))































