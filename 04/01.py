from functools import total_ordering
from math import sqrt, pi
from tkinter import N
def area(r,shape_constant):
    assert r>0,'math is broken'
    return r*shape_constant
def area_circle(r):
    return area(r,pi)
def area_hexagon(r):
    return area(r,3*sqrt(3)/2)
k=area_circle(10)  
def jiefangcheng(a,b,c):
    assert (b*b-4*a*c)>=0,'没有实数根'
    return (-b+sqrt(b*b-4*a*c))/2, (-b-sqrt(b*b-4*a*c))/2
def sum_naturals(n):
    total,k=0,1
    while k<=n:
        total,k=total+k,k+1
    return total
def sum_cubes(n):
    toatl,k=0,1
    while k<=n:
        total,k=total+pow(k,3),k+1
    return total
def cube(k):
    return pow(k,3)
def summation(n,term):
    total,k=0,1
    while k<=n:
        total,k=total+term(k),k+1
    return total

def make_adder(n):
    '''***return a fuction as a value'''
    def adder(k):
        return k+n
    return adder
def search(f):
    x=0
    while True:
        if f(x):
            return x
        x+=1
def is_three(x):
    return x==3
def square(x):
    return x*x
def positive(x):
    return max(0,square(x)-100)
search(positive)
def inverse(f):
    '''*****a fuction(g(y)) that return x which makes f(x)==y    即反函数'''
    return lambda y:search(lambda x:f(x)==y)
sqrt=inverse(square)
'''新格式： <consequent>if<predicate)else<alternative>
ex:
>>>x=0
>>>abs(1/x if x!=0 else 0
0'''



    
        
        