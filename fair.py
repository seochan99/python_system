num = int(input())
for i in range(num):
    print(" "*i+"*"*((num-i)*2-1))
for i in range(1,num):
    print(" "*(num-i-1)+"*"*(i*2+1))