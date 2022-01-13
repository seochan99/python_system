#1920 : 수찾기
# import sys
# sys.setrecursionlimit(10**6)
# input = sys.stdin.readline

# def bsr(target,start,end,data):
#     if start>end:
#         return None
#     mid = (start+end)//2
#     if data[mid]==target:
#         return 1
#     elif data[mid]>target:
#         end = mid - 1
#     else : #data[mid]<target
#         start = mid + 1 
#     return bsr(target,start,end,data)

# num1 = int(input())
# arr1 = list(map(int,input().split()))
# num2 = int(input())
# arr2 = list(map(int,input().split()))
        
# #이분탐색 
# arr1.sort()

# for i in range(num2):
#     if bsr(arr2[i],0,num1-1,arr1):
#         print(1)
#     else :
#         print(0)

#10989 : 수 정렬하기 3
# import sys
# input = sys.stdin.readline
# n = int(input())

# check=[0]*10001 

# for _ in range(n):
#     num = int(input())
#     check[num] +=1

# for i in range(10001):
#     if check[i]!=0: 
#         for _ in range(check[i]):
#             print(i)

#숫자 카드
# import sys
# input=sys.stdin.readline
# sys.setrecursionlimit(10**4) 

# #이분탐색 
# def bsr(target,start,end,data): #
#     if start>end:
#         return None
#     mid = (start+end)//2
#     if data[mid]==target:
#         return 1
#     elif data[mid]>target:
#         end = mid - 1
#     else : #data[mid]<target
#         start = mid + 1 
#     return bsr(target,start,end,data)

# n = int(input()) #상근 카드 갯수 
# arr1 = list(map(int,input().split()))

# m = int(input()) #엠
# arr2 = list(map(int,input().split()))

# #상근이가 가지고 있으면 1 아니면 0 출력 
# arr1.sort()
# for i in range(m):
#     if bsr(arr2[i],0,n-1,arr1):
#         print(1,end=" ")
#     else :
#         print(0,end=" ")

# #10876: 중복빼고 정ㅕ 
# n = int(input())
# arr = list(map(int,input().split()))

# #중복제거를 위한 집합으로 받기 
# for i in sorted(list(set(arr))):
#     print(i,end=" ")


# # 삽입 
# color1.append("black")
# color1.extend(["white","orange"])
# color1.insert(2,"purple")
# color1.append("green")
# print(color1)
# #제거 
# color1.remove("green")
# del color1[0]
# print(color1)

# a = [5,5,3,4,1,2]
# b = ["b","c","a"]
# print(a)
# print(a.index(2))
# print(a.count(5))
# # a.sort() #오름차순
# # a.sort(reverse=True) #내림차순 
# # a.reverse() #문자열 역으로 출력 
# b=sorted(a)

# print(a)
# print(b)

#패킹 
test = [1,2,"apple"]
a,b,c = test
print(a,b,c) 
print(test)

