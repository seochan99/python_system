
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

from bisect import bisect_left, bisect_right 

def count_by_range(a,left_value,right_value):
    right_idx = bisect_right(a,right_value)
    left_idx = bisect_left(a,left_value)
    return right_idx - left_idx 

n,x = map(int,input().split())
arr = list(map(int,input().split())) 

# 값이 4인 데이터 개수 출력 
result = count_by_range(arr,x,x)
print(result if result else -1)

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