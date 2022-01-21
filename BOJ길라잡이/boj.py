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
# test = [1,2,"apple"]
# a,b,c = test
# print(a,b,c) 
# print(test)

#18406 


# score =input()
# halfLength = len(score)//2 
# front = score[:halfLength] ; back = score[halfLength:]
# frontScore = 0 ; backScore = 0 

# for fronts in front:
#     frontScore+=int(fronts)
# for backs in back:
#     backScore+=int(backs)

# if frontScore == backScore:
#     print("LUCKY")
# else :
#     print("READY")

# score = input()
# front,back = 0,0 
# for i in score[:len(score)//2]:front+=int(i)
# for i in score[len(score)//2:]:back+=int(i)
# print("LUCKY" if front==back else "READY")
    

#문자열 재정렬 
munja = input()
ans = []
score = 0 

for x in munja:
    if x.isalpha():
        ans.append(x) 
    else :
        score+=int(x)

ans.sort()
if score!=0:
    ans.append(str(score))
print(''.join(ans))

#문자열 압축 
#압축전 s 
#압축을 시도해서 가장 짧은 것의 길이 return 하는 함수 작성
ldd =[]
def solution(munja):
    cnt=0
    for i in range(len(munja)-1):
        if munja[i]==munja[i+1]:
            cnt += 1 
            del munja[i]
        else :
            ldd.append([cnt,munja[i]])
            cnt = 1 
    return ldd
munja = list(input())

print(solution(munja))


#문자열 압축 
#aabbaccc 
#2a2ba3c 
#반복적으면 압축률 낮음 
#2개이상단위로 자르는 방법 생각 
#ababcdcdababcdcd
#2ab2cd2ab2cd(2개)
#2ababcdcd(8개) -> 제일 짧음 





