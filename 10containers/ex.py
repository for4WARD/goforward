
def count(s,value):
    """return the number of times value appearing in s"""
    total=0
    for i in s:
        if i ==value:
            total +=1
    return total
odds=[1,1,1,2,3,4]


# 分割线——————

city = "berkeley"
print(city[3])

def reverse(L):
    if len(L)==1:
        return L
    else:
        return reverse(L[1:])+L[0]
    
print(reverse("ward"))




