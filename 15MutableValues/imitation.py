



a='焯'
b='操'
c='优美的中国话:'
print(ord(b),ord(a))
def my(s):
    s.pop()
    
four=[1,2,3,4]
Four=four
four.append(5)

print(Four)
print(c,b,a)
h=float('inf')

x=min(h,2)
print(x)
a=str([-1,-2])
x_2=2
x_1=x_2
print()
def move_disk(disk_number,start_peg,end_peg):
	print ("move disk "+str(disk_number)+" from start peg "+str(start_peg)+" to end peg "+str(end_peg))
def hanoi(n,start_peg,end_peg):
    if n==1:
        move_disk(n,start_peg,end_peg)
    else:
        spare_peg=6-start_peg-end_peg
        hanoi(n-1,start_peg,spare_peg)
        move_disk(n,start_peg,end_peg)
        hanoi(n-1,spare_peg,end_peg)
print(hanoi(3, 2,1))