# # # def d(n):
# # #     a = 0
# # #     for x in list(str(n)): #i를 받고 리스트만큼 반복  1 5 7 
# # #         a = a + int(x)  #각각 더하기 
# # #     return int(n) + a #셀프넘버 말고 구하기

# # # a= [] # 배열 선언 

# # # for i in range(1,10001):
# # #     k = d(i) #i 를 d 함수에 넣기 
# # #     a.append(k)

# # # #a=[1,2,3,4,5,40]
# # # for b in range(1, 10001):
# # #     if b in a:
# # #         pass
# # #     else:
# # #         print(b) #셀프넘버만 출력 ,생성자가 없는 케이스 




# # ###


# # # n = int(input())
# # # han = 0
# # # for i in range(1, n + 1):
# # #     if i < 100: # 100밑으로는 모두 한수 
# # #         han += 1
# # #     else:
# # #         ns = list(map(int, str(i)))
# # #         if ns[0] - ns[1] == ns[1] - ns[2]: # 123  ns[0] = 1, ns[1] = 2, ns[2] = 3 
# # #             han += 1
# # # print(han)

# # # 벌집 

# # n = int(input()) # 입력받기 

# # num_bulzip = 1  #벌집개수
# # cnt = 1

# # while n > num_bulzip :
# #     num_bulzip += 6 * cnt  # 벌집이 6의 배수로 증가
# #     cnt += 1  
# # print(cnt) #총횟수 출력



# # #호텔
# # n = int(input())
# # for _ in range(int(input())):
# #     h,w,p = map(int,input().split())
# #     a = n % h ; b = n//h+1
# #     if a==0 : a=h ; b-=1
# #     print(a*100+b)







# # # #달팽이
# # a, b, v = map(int, input().split())
# # day = 0
# # #0이 아니라면 아직 도착한것이 아니다 ! +1 해준다 
# # if (v - b) % (a - b) != 0: #목표지점도달시 미끌x => v-b만큼의 높이를 올라가면된다. 
# #     day = ((v - b) // (a - b)) + 1
# # #0이라면 몫출력한다 
# # else:
# #     day = ((v - b) // (a - b)) # a-b만큼올라간다 하루마다 
# # print(day)










# # #부녀회 
# # T = int(input()) #테스트케이스 받기 

# # for _ in range(T): #테스트케이스만큼 반복 
# #     k = int(input()) #k층
# #     n = int(input()) #n호
# #     people = [ i for i in range(1, n+1)]  #리스트 포문작성[표현식 for 항목 in 리스트(range)] [0,1,2....]
# #     for __ in range(k): #층만큼
# #         for j in range(1,n): #호만큼
# #             people[j] += people[j-1] 
# #     print(people[-1]) #오른쪽 끝 요소 출력 


# # n=int(input())

# # ans=0
# # for i in range(n): #n만큼 반복 
# #     word = input() #단어 입력받음 
# #     for j in range(len(word)):
# #         if j!=len(word)-1: #단어의 끝도달전
# #             if word[j]==word[j+1]: #옆에 같은 문자 있을 시 패스 
# #                 pass
# #             elif word[j] in word[j+1:]: #옆이 아닌 다른곳에 있을 시 브레이크 
# #                 break 
# #         else:
# #             ans +=1 # 브레이크없이 끝날경우 ans +=1 진행
# # print(ans)

# #2839

# # n = int(input())
# # cnt=0 #봉지 최소 갯수 

# # while True: #무한 반복  
# #     if(n%5)==0: #5의배수 
# #         cnt += (n//5)
# #         print(cnt)
# #         break
# #     n-=3 #5의 배수가 아닐 때 매번빼주기 
# #     cnt+=1 
# #     if n<0 : #n이 0미만 
# #         print(-1)
# #         break 

# #10757

# # a, b = map(int, input().split())
# # print(a+b)

# # #1011
# # test = int(input())#테스트 케이스

# # for i in range(test):
# #     x,y = map(int,input().split()) #x,y받기 
# #     distance = int(y-x) #사이 거리 
# #     cnt =0 #작동횟수  

# # # 7.18 규칙찾는중,,,

# #1978
# # n = int(input()) # 주어진 수 
# # nums = map(int,input().split())
# # prime=0
# # for num in nums:
# #     notPrime =0
# #     if num > 1:
# #         for i in range(2,num): #2~num-1까지
# #             if num % i == 0:
# #                 notPrime+=1 #소수가 아닌 수를 발견하면 하나 올린다 
# #         if notPrime ==0: 
# #             prime +=1 
# # print(prime)

# # #2581 
# # m = int(input())
# # n = int(input())

# # prime_list = []
# # for num in range(m,n+1):
# #     notPrime =0 
# #     if num>1:
# #         for i in range(2,num): #2~num-1까지 
# #             if num % i == 0:
# #                 notPrime+=1
# #                 break
# #         if notPrime == 0 :
# #             prime_list.append(num) #소수 추가 

# # if len(prime_list)>0:
# #     print(sum(prime_list))
# #     print(min(prime_list))
# # else:
# #     print(-1)    

# #11653
# # n = int(input()) 
# # j=2 #2부터 
# # while n!=1 : #n이 1이되기전까지 반복 
# #     if n%j==0:
# #         n/=j
# #         print(j)
# #     else:#j=2일때 불능하다면 +1씩 올려간다 ! 
# #         j+=1 

# #1929

# #시간초과
# # m, n = map(int,input().split())
# # for j in range(m,n+1):
# #     notPrime=0
# #     if j>1:
# #         for i in range(2,j):
# #             if j%i==0:
# #                 notPrime+=1
# #                 break
# #         if notPrime == 0:
# #             print(j)

# #에라토스테네스의 체 활용 

# # def prime_list(k,n):
# #     n+=1 #n이하의 숫자를 확인해야하므로 ! 
# #     # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
# #     sieve = [True] * n
# #     # n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
# #     m = int(n ** 0.5)
# #     for i in range(2, m + 1):
# #         if sieve[i] == True:           # i가 소수인 경우 참 
# #             for j in range(2*i, n, i): # i이후 i의 배수들을 False 판정
# #                 sieve[j] = False
    
# #     for i in range(k,n):
# #         if i>1 and sieve[i]==True:
# #             print(i)

# # m,n = map(int,input().split())

# # prime_list(m,n)

# # #1011 
# # t = int(input())

# # for _ in range(t):
# #     x,y = map(int,input().split())
# #     distance = y -x 
# #     num =1 
# #     while True :
# #         if num**2<= distance < (num+1)**2:
# #             break 
# #         num+=1 #제곱수 num찾기 
# #     if num**2 == distance:
# #         print((num*2)-1) 
# #     elif num**2 < distance <= num**2+num:
# #         print(num*2) #절반 
# #     else:
# #         print((num*2)+1)

# #4948
# def prime_list(k,n):
#     n+=1 #n이하의 숫자를 확인해야하므로 ! 
#     # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
#     sieve = [True] * n
#     # n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
#     m = int(n ** 0.5)
#     count=0
#     for i in range(2, m + 1):
#         if sieve[i] == True:           # i가 소수인 경우 참 
#             for j in range(2*i, n, i): # i이후 i의 배수들을 False 판정
#                 sieve[j] = False
    
#     for i in range(k,n):
#         if i>1 and sieve[i]==True:
#             count+=1
#     print(count)

# while True:
#     num = int(input())
#     if num == 0 :
#         break
#     else :
#         prime_list(num+1,num*2)



# #9020 : 골드바흐의 추측 

# def prime_list(n): #소수 판독기 
#     n+=1 #n이하의 숫자를 확인해야하므로 ! 
#     # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
#     primeList = [True] * n
#     # n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
#     m = int(n ** 0.5)
#     for i in range(2, m + 1):
#         if primeList[i] == True:           # i가 소수인 경우 참 
#             for j in range(2*i, n, i): # i이후 i의 배수들을 False 판정
#                 primeList[j] = False

#     return [i for i in range(2,n) if primeList[i]==True] #소수반환  
    

# def total(n):
#     list = prime_list(n) #15 2,3,5,7,11,13
#     idx = max([i for i in range(len(list)) if list[i]<=n/2]) #최댓값 list길이 만큼 for 실행 그런데..n/2이하일경우 최대인 인덱스값 출력 
#     for i in range(idx,-1,-1): #인덱스 이하의 배열 요소 접근 
#         for j in range(i,len(list)): #i이상의 배열 요소 접근 
#             if list[i]+list[j]==n: #합 비교 
#                 return [list[i],list[j]] #소수 찾기 성공 

# test = int(input()) 
# for _ in range(test):
#     a = int(input())
#     print(" ".join(map(str,total(a)))) #join으로 나타내주기 

# #1085
# x,y,w,h = map(int,input().split()) # x,y,w,h 값 입력받기 
# print(min(x,y,h-y,w-x))

# #3009 

# xList=[]
# yList=[]
# #x,y리스트받기 
# for i in range(3):
#     x,y = map(int,input().split())
#     xList.append(x)
#     yList.append(y)

# for i in range(3):
#     if xList.count(xList[i]) == 1: #x 1개인 요소 찾기 
#         x = xList[i]
#     if yList.count(yList[i]) == 1: #y 1개인 요소 찾기 
#         y = yList[i]

# print(f"{x} {y}")

# #4153

# while True :
#     length = list(map(int,input().split()))
#     if sum(length)==0:
#         break
#     max_len = max(length)
#     length.remove(max_len) #긴 길이 지우기 
#     if (length[0]**2 + length[1]**2 == max_len**2):
#         print("right")
#     else:
#         print("wrong")

# #3053
# import math 
# r = int(input())
# print(r*r*math.pi)
# print(r*r*2)

# #1002 

# test = int(input())
# for _ in range(test):
#     x1,y1,r1,x2,y2,r2 = map(int,input().split())
#     distance = ((x1-x2)**2 +(y1-y2)**2)**(1/2)
#     maxR=r1+r2
#     minR=abs(r1-r2) 
#     if distance==0:
#         if r1 == r2: #원이 겹치는 경우 
#             print(-1) 
#         else : #원이 접하지 않는 경우 
#             print(0)
#     else:
#         if distance == maxR or distance == minR:
#             print(1)
#         elif distance<maxR and distance > minR: # 
#             print(2)
#         else : #아예 딴 곳 
#             print(0) 


# #10872 : 팩토리얼 

# # def fact(n):
# #     if n==1:
# #         return 1
# #     return n*fact(n-1)

# # num = int(input())
# # if num==0:
# #     print(1)
# # else :
# #     print(fact(num))

# #10870 : 피보나치수열 

# # def fibo(n):
# #     if n<=1:
# #         return n
# #     return fibo(n-2)+fibo(n-1)

# # num = int(input())
# # print(fibo(num))

# #2447
# n, m = map(int,input().split())
# arr = list(map(int,input().split()))
# total = 0
# for i in range(n):
#     for j in range(i+1,n):
#         for k in range(j+1,n):
#             if arr[i]+arr[j]+arr[k]>m:
#                 continue
#             else :
#                 total = max(total,arr[i]+arr[j]+arr[k])
# print(total)

#2447 : 별찍기 
# def MakeStarList(n):
#     arr=[]
#     #num == 9일때 len(n) == 3 
#     for i in range(3*len(n)):
#         if i//len(n)==1: #몫이 1일때 
#             arr.append(n[i%len(n)]+" "*len(n)+n[i%len(n)])
#         else : # 몫이 다른 값일 경우 stars로 채움 
#             arr.append(n[i%len(n)]*3) 
#     return (list(arr))

# stars=["***","* *","***"]  #디폴트 패턴 

# num = int(input())
# count = 0
# while num != 3:
#     num = int(num/3)
#     count+=1 #제곱수 - 1 구하기 

# for _ in range(count):
#     stars = MakeStarList(stars)

# for i in stars:
#     print(i) 

# print('\n'.join([''.join([str(i) for i in row]) for row in arr]))

# #11729 : 하노이 탑 이동 순서 
# def HanoiTowerMove(num,_from,by,to):
#     #이동해야 할 원반의 수가 1개일 경우 재귀 탈출 
#     if(num==1):
#         print(f"{_from} {to}")
#     else :
#         HanoiTowerMove(num-1,_from,to,by) #n-1개 옮기기 
#         print(f"{_from} {to}")
#         HanoiTowerMove(num-1,by,_from,to)

# num=int(input())
# print(2**num-1) # 하노이탑 최소이동횟수 : 2^num - 1 
# HanoiTowerMove(num,1,2,3)

#2231 : 분해합
#브루트포스 무식 하게 
# num = int(input())

# BunHaeHap = 0 #분해합 

# for i in range(1,num+1):
#     con = list(map(int,str(i))) #i의 각자리수 리스트에 삽입 
#     BunHaeHap = i + sum(con) # 분해합 
#     if BunHaeHap == num :
#         print(i)
#         break
#     if i==num:
#         print(0)

#7568
#1 왜 안될까.... 하 
# num = int(input())
# all_list =[[0]*2 for i in range(num)]  #리스트표현식 
# #[0,0] 을 넘만큼 생성한 list = all_list 

# #무게,키 넣기 
# for i in range(num):
#     x, y = map(int,input().split())
#     all_list[i][0] = x
#     all_list[i][1] = y

# for i in range(num):
#     count = 0
#     for j in range(num):
#         if all_list[i][0]<all_list[j][0] and all_list[i][1]<all_list[j][1] :
#             count += 1
#     print(count+1,end=' ')

#2 append 
# test = int(input())
# arr = []
# for i in range(test):
#     x, y = map(int,input().split())
#     arr.append((x,y))

# for i in arr: #리스트 직접접근 
#     count = 0
#     for j in arr:
#         if i[0]<j[0] and i[1] < j[1]:
#             count+=1
#     print(count+1,end =' ') 

    

#1436
# n = int(input())
# count = 0 
# sixsixsix= 666
# while True:
#     if '666' in str(sixsixsix):
#         count+=1
#     if count == n:
#         print(sixsixsix)
#         break
#     sixsixsix+=1

#3046 : R2
# R1, S = map(int,input().split())
# print(S*2 - R1)

#2163
# n, m = map(int,input().split())
# print(n*m-1)

#10699 : 오늘 날짜
# from datetime import datetime
# print(datetime.today().strftime("%Y-%m-%d"))

#7287 : 등록 
# print("80\n")
# print("gmlcks0513")

# 2525 : 오븐 시계
# a, b, c= map(int,input().split())
# t = int(input()) #걸리는 시간(초단위)

# c+= t%60
# t = t//60
# if c>=60:
#     b+=1
#     c-=60

# b+=t%60
# t = t//60
# if b>=60:
#     a+=1
#     b-=60

# a+=t%24
# if a>=24:
#     a-=24
# print(a,b,c)

# 2914 : 저작권 
# a, i = map(int,input().split())
# print(a*(i-1)+1)

#5355 : 화성 수학 
# @ = *3 % +5 #=-7
# test = int(input())
# for _ in range(test):
#     arr = list(map(str,input().split())) #배열로 입력받기
#     ans = 0
#     for i in range(len(arr)):
#         if i==0:
#             ans+=float(arr[i])
#         else :
#             if arr[i] == '#':
#                 ans-=7
#             elif arr[i] == '@':
#                 ans *=3
#             elif arr[i] == '%':
#                 ans +=5
#     print('%0.2f' %ans)

#2935
# a=int(input())
# b=input()
# c=int(input())

# if b=="*":
#     print(a*c)
# else:
#     print(a+c)

#10817
# arr = list(map(int,input().split()))
# arr.sort()
# print(arr[1])

#1789 
# num = int(input())
# n=1
# while n*(n+1)/2<=num:
#     n+=1
# print(n-1)

#10039 
# arr=[0,0,0,0,0]
# sum=0
# for i in range(5):
#     arr[i]= int(input())
#     if arr[i]<=40:
#         arr[i]=40
#     sum+=arr[i]
# print(sum//5)


#1934
# def gcd(a, b):
#     return gcd(b, a % b) if b else a
# def lcm(a, b):
#     return a * b // gcd(a, b)

# test = int(input())
# for i in range(test):
#     a,b = map(int,input().split())
#     print(lcm(a, b))
# # 최소공배수 = 두 수 곱 / 최대 공약수 

#1018 : 체 스 으 .. 
# n, m = map(int,input().split()) #세로 가로
# arr =[[0]*m for i in range(n)] 
# count=0
# for i in range(n):
#     arr[i]=input() #BW 입력 받기     
#     for j in range(0,m):
#         if arr[i][j] == arr[i][j+1]:
#             count+=1
# print(count)

#2480
# arr = list(map(int,input().split()))
# if arr[0]==arr[1]==arr[2] :
#     print(10000+arr[0]*1000)
# elif arr[0]==arr[1] or arr[0]==arr[2] :
#     print(1000+arr[0]*100)
# elif arr[1]==arr[2] :
#     print(1000+arr[1]*100)
# else :
#     print(max(arr)*100)

#4101 : 크냐 ?
# while True :
#     a, b = map(int,input().split())
#     if a==0 and b==0:
#         break
#     if a>b:
#         print("Yes")
#     else:
#         print("No")

#10156 : 과자

# k,n,m = map(int,input().split())
# cracker = k*n
# if cracker>m:
#     print(cracker-m)
# else :
#     print(0)

#2476 : 주사위 게임
# n = int(input())
# maxN=[0]*n
# for i in range(n) :
#     arr = list(map(int,input().split()))
#     if arr[0]==arr[1]==arr[2] :
#         maxN[i]=10000+arr[0]*1000
#     elif arr[0]==arr[1] or arr[0]==arr[2] :
#         maxN[i]=1000+arr[0]*100
#     elif arr[1]==arr[2] :
#         maxN[i]=1000+arr[1]*100
#     else :
#         maxN[i]=max(arr)*100
# print(max(maxN))

#2754 : 학점계산 
# grade = {
#     "A+":4.3,"A0":4.0,"A-":3.7,
#     "B+":3.3,"B0":3.0,"B-":2.7,
#     "C+":2.3,"C0":2.0,"C-":1.7,
#     "D+":1.3,"D0":1.0,"D-":0.7,
#     "F":0.0
# }

# print(grade[input()])

#7567 : 그릇 
# arr = list(str(input()))
# length=10
# for i in range(1,len(arr)):
#     if arr[i-1]==arr[i]:
#         length+=5
#     else :
#         length+=10
# print(length)

#5063 : TGN
# test = int(input())
# for _ in range(test):
#     r,e,c = map(int,input().split())
#     inv = e-c
#     if inv>r :
#         print("advertise")
#     elif inv == r :
#         print("does not matter")
#     else :
#         print("do not advertise")

#10102 : 개표 
# num = int(input())
# arr = list(str(input()))

# a=0 ; b=0

# for i in range(num):
#     if arr[i]=='A':
#         a+=1
#     elif arr[i]=='B':
#         b+=1
# if a>b:
#     print('A')        
# elif b>a:
#     print('B')
# else :
#     print("Tie")

# 10886 : 준희야
# n = int(input())
# cute = 0 ; notCute=0
# for _ in range(n):
#     ppl=int(input())
#     if ppl ==0:
#         notCute+=1
#     elif ppl == 1:
#         cute += 1
# if cute>notCute:
#     print("Junhee is cute!")
# else :
#     print("Junhee is not cute!")

# 10988 : 펠린드롬인지 확인하기
lang = list(str(input()))
if list(reversed(lang))==lang :
    print(1)
else :
    print(0)
