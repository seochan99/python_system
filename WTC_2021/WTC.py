#1
def solution(arr):
    num=[0,0,0,0]
    ans =[0,0,0]
    for i in arr:
        if i==1:
            num[0]+=1
        elif i == 2:
            num[1]+=1
        else :
            num[2]+=1 
    num[3]=max(num)
    ans[0]=num[3]-num[0]
    ans[1]=num[3]-num[1]
    ans[2]=num[3]-num[2]
    # for i in range(num1):
    #     arr.append(1)
    return ans 

arr = [2,1,3,1,2,1]
print(solution(arr))
