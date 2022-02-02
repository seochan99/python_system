# def fibo(x):
#     if x==1 or x==2:
#         return 1 
#     return fibo(x-1)+fibo(x-2)
# print(fibo(4))

# d = [0]*100 

# def fibo(x):
#     if x==1 or x==2:
#         return 1
#     if d[x] !=0:
#         return d[x]
#     d[x] = fibo(x-1) + fibo(x-2)
#     return d[x]
# print(fibo(99))

# d = [0] * 100
# d[1] = 1 
# d[2] = 1 
# n = 99
# for i in range(3,n+1):
#     d[i] = d[i-1]+d[i-2]

# print(d[n])

# n = int(input())
# arr = list(map(int,input().split()))

# d = [0]*100 

# d[0] = arr[0]
# d[1] = max(arr[0],arr[1])
# for i in range(2,n):
#     d[i] = max(d[i-1],d[i-2]+arr[i]) 
# print(d[n-1])

x = int(input())
d=[0]*30001 

for i in range(2,x+1):
    d[i] = d[i-1]+1 
    if i%2==0:
        d[i] = min(d[i],d[i//2]+1)
    if i%3==0:
        d[i] = min(d[i],d[i//3]+1)
    if i%5==0:
        d[i] = min(d[i],d[i//5]+1)
print(d[i])