
#이진 탐색 : 재귀 
# def bs(arr,target,start,end):
#     if start>end:
#         return None
#     mid = (start+end)//2 
#     if arr[mid]==target:
#         return mid 
#     elif arr[mid]>target:
#         return bs(arr,target,start,mid-1) 
#     else :
#         return bs(arr,target,mid+1,end)

# n,target = list(map(int,input().split()))

# arr = list(map(int,input().split()))

# result = bs(arr,target,0,n-1)
# if result==None:
#     print("원소X")
# else:
#     print(result+1)
#이진 탐색 : 반복 

# def bs(arr,target,start,end):
#     while start<=end:
#         mid = (start+end)//2
#         if arr[mid]==target:
#             return mid 
#         elif arr[mid]>target:
#             end = mid -1 
#         else :
#             start = mid + 1
#     return None

# n,target = list(map(int,input().split()))

# arr = list(map(int,input().split()))

# result = bs(arr,target,0,n-1)
# if result==None:
#     print("원소X")
# else:
#     print(result+1)

# from bisect import bisect_left, bisect_right 

# def findRange(a,left_value,right_value):
#     right_idx = bisect_right(a,right_value)
#     left_idx = bisect_left(a,left_value)
#     return right_idx - left_idx 

# n = int(input())
# arr1 = list(map(int,input().split())) 
# arr1.sort()
# m = int(input())
# arr2 = list(map(int,input().split())) 

# for find in arr2:
#     print(findRange(arr1,find,find),end=" ")


# -1~3범위에 있는 데이터 개수 출력 
# print(count_by_range(a,-1,3)) 






# n,m = map(int,input().split())
# arr = list(map(int,input().split()))

# start = 0 ; end = max(arr)

# result=0
# while start<=end:
#         total = 0
#         mid =(start+end)//2 
#         for x in arr: #떡 자른 양 계산하기 
#             if x> mid:
#                 total += x -mid 
#         # 떡 양이 부족한 경우 더 많이 자르기(왼쪽 부분 탐색)
#         if total<m:
#             end = mid - 1 
#         # 떡 양이 충분한 경우 덜 자르기 (오른쪽 부분 탐색)
#         else : 
#             result = mid  #최대한 덜 잘랐을때가 답이므로 기록계속 갱신 
#             start = mid + 1

# print(result)

#### 1072 : 게임 
#### 해설용 
# x,y = map(int,input().split()) 
# # x : 잔체 게임 y : 이긴 게임 
# avg = (y/x)*100
# findAvg = avg+1 

# if(avg>=100):
#     print(-1)
#     exit()
# print("findAvg : ",findAvg)

# start = 1 ; end = x 

# while start<=end:
#     mid = (start+end)//2
#     print("mid : ",mid)
#     newAvg = ((y+mid)/(x+mid))*100
#     print("newAvg : ",newAvg)
#     if newAvg<findAvg:
#         start = mid+1 
#     else :
#         result = mid 
#         end = mid - 1 

    
# print(result)
# import math 
# import sys 
# input = sys.stdin.readline

# x,y = map(int,input().split()) 
# # x : 잔체 게임 y : 이긴 게임 
# avg = (y*100/x) ; findAvg = math.floor(avg)+1

# if(avg>=100):
#     print(-1)
#     exit(0)

# start = 0 ; end = x 

# while start<=end:
#     mid = (start+end)//2
#     newAvg = (((y+mid)*100)/(x+mid))
#     if newAvg<findAvg:
#         start = mid+1 
#     else :
#         result = mid 
#         end = mid - 1 

# print(result)

# 제곱근
# n = int(input())

# start = 1
# end = n 
# while start<=end:
#     mid = (start+end)//2
#     find=mid*mid
#     if n==find:
#         print(mid)
#         break 
#     elif n>find:
#         start = mid + 1
#     else :
#         end = mid - 1 

# 1654 : 랜선자르기 
# k,n = map(int,input().split())
# line = [] ; result = []

# for _ in range(k):
#     line.append(int(input()))

# start = 1 ; end = max(line)

# while start<=end:    
#     total = 0
#     mid =(start+end)//2 
#     for x in line: 
#             total += x//mid
#     if total>=n:
#         start = mid + 1 
#     else : #부족할때 
#         end = mid - 1 
# print(end)

# 2512 : 예산 
# from re import T


# n = int(input())
# asset = list(map(int,input().split()))
# chongAsset = int(input())

# start,end = 0,max(asset)
# result = []
# while start<=end:
#         mid =(start+end)//2 
#         total =0 
#         for x in asset:
#             if x<mid:
#                 total+=x   
#             else :                                 
#                 total+=mid 
#         if total<=chongAsset:
#             start = mid + 1 
#         else : 
#             end = mid - 1
            

# print(end)
# n,m = map(int,input().split()) #강의수 #M개의 블루레이         .
# time = list(map(int,input().split()))

# # 블루레이크기를 이분탐색하자 ! 
# start,end = max(time),sum(time)
# result = end

# while start<=end:
#     mid = (start+end)//2 
    
#     total =0 ; cnt = 0
#     for times in time:
#         if total+times > mid:
#             cnt+=1 
#             total=0 
#         total += times 
#     if total: # 토탈이 남아있다면 
#         cnt+=1 #1개추가 

#         # print(f"start : {start} mid : {mid} end : {end}, cnt {cnt}")
#     if cnt<=m: #총 개수가 블루레이보다 작거나 같다 
#         result = min(result,mid)
#         end = mid - 1
#     else :
#         start = mid + 1
        
# print(result)
    

#2792 : 보석 상자 
#질투심 = 가장 많은 보석을 가져간 애의 보석의 수  -> 질투심 최소가되게 찾자 
# 보석 최소 
# 항상 같은 색 보석만 
# n,m = map(int,input().split()) #학생의 수 n ->

# jew = []
# for i in range(m):
#     jew.append(int(input()))

# start,end = 1,max(jew) 

# result = end

# while start<=end:
#     mid = (start+end)//2 
#     total=0;cnt = 0 # cnt = 아이 수 
#     for jews in jew:
#         for _ in range(jews):
#             one = 1
#             if total+one>mid:
#                 cnt+=1
#                 total=0
            
#             total += i 
#         if total: # 토탈이 남아있다면 
#             total=0
#             cnt+=1 #1개추가 

#         print(f"start : {start} mid : {mid} end : {end}, cnt {cnt}")
#     if cnt<=n:
#         start = mid + 1
#         result = min(result,mid)
#     else :
        
#         end = mid - 1
        
# print(result)
# n = int(input())
# yeahsan = list(map(int,input().split()))
# chongYeahsan = int(input())

# start,end = 0,max(yeahsan)

# while start<=end:
#     mid = (start+end)//2 
#     total=0 
#     for x in yeahsan:
#         if x>=mid :
#             total += mid 
#         else : 
#             total += x 
#     if total<=chongYeahsan: 
#         start = mid + 1 
#     else :
#         end = mid - 1 

# print(end)

# n = int(input())
# start = 1 
# end = n 

# while start<=end:
#     mid = (start+end)//2
#     imFind = mid*mid
#     if imFind == n :
#         print(mid)
#         break 
#     elif imFind < n:
#         start = mid + 1 
#     else :
#         end = mid - 1 



# list = ["서희찬","이건회","박현준"]
# ran_num = random.randint(1,3)

# for i in range(3):
#     while ran_num in list:
#         ran_num = random.randint(1,3)
#     list.append(ran_num)

# print (list)



n = int(input())

start = 1
end = n 

while start<=end:
    mid = (start+end)//2
    target = mid**2 
    if target==n:
        print(mid)
        break 
    elif n>target:
        start = mid + 1 
    else :
        end = mid - 1







