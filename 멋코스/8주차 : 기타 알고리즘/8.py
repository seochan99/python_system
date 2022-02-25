n = int(input())
arr = list(map(int,input().split()))
x = int(input())
arr.sort()

left, right = 0, n-1
ans = 0 

while left<right:
    temp = arr[left] + arr[right]  # temp left,right 값 저장 
    if temp == x:
        ans+=1 
    if temp<x:
        left+=1 
        continue 
    right -= 1 
print(ans)



