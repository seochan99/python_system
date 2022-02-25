#소수판별
def prime(n):
    for i in range(2,n):
        if i*i>n:
            break 
        if n%i == 0:
            return False 
    return True 
    
n = int(input())
numbers = set(map(int,input().split()))

ans = 1
for n in numbers:
    if prime(n):
        ans*=n 

if ans==1 :#prime x
    print(-1)
else :
    print(ans)