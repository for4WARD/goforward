def sum_last_num(n):
    if n<10:
        return n
    else:
        n,last_num=n//10,n%10
        return sum_last_num(n)+last_num
def luhn_algorithm(n):
    if n%2==0:
        n=n*2
        if n>9:
            n=sum_last_num(n)
            return n
        else:
            return n
    else:
        return n
        
def luhn_sum(n):
    if n<10:
        return luhn_algorithm(n)
    else:
        n,last_num=n//10,luhn_algorithm(n%10)
        return sum_last_num(n)+last_num
def inverse_cascade(n):
    grow(n)
    print(n)
    shrink(n)
def f_then_g(f,g,n):
    if n:
        f(n)
        g(n)
grow = lambda n:f_then_g(grow,print,n//10)
shrink=lambda n:f_then_g(print,shrink,n//10)

def sum_x(*args):
    s=0
    for arg in args:
        k=arg 
        s=s+k
        print(s)




nums=(1,2,3,4,6)

def sum_y(*args):
    s=0
    for arg in args:
        k=arg 
        s=s+k
        print(s)
print (sum_y(nums))



    
    




























