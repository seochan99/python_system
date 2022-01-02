# # # def d(n):
# # #     a = 0
# # #     for x in list(str(n)): #i를 받고 리스트만큼 반복  1 5 7 
# # #         a = a + int(x)  #각각 더하기 
# # #     return int(n) + a #셀프넘버 말고 구하기

# # # a= [] # 배열 선언 

# # # for i in range(1,10001):
# # #     k = d(i) #i 를 d 함수에 넣기 
# # #     a.append(k)

#a=[1,2,3,4,5,40]
# for b in range(1, 10001):
#     if b in a:
#         pass
#     else:
#         print(b) #셀프넘버만 출력 ,생성자가 없는 케이스 




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
# all_list =[[0]*2 for i in range(num)]  

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
# #쪼개기 (N-7),(M-7)
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
# lang = list(str(input()))
# if list(reversed(lang))==lang :
#     print(1)
# else :
#     print(0)

#
# while True:
#     m,n = map(int,input().split())
#     if m==0 and n==0 :
#         break 
#     print(m+n)
    

#5086 : 배수와 약수 
# while True :
#     m,n = map(int,input().split())
#     if m==0 and n==0 : #탈출 
#         break 
#     if n%m==0 :
#         print("factor")
#     elif m%n==0 :
#         print("multiple")
#     else :
#         print("neither")

#9610 : 사분면
# t = int(input())
# q1 = 0 ; q2 =0 ; q3 =0 ; q4=0 ; axis =0
# for i in range(t):
#     x,y = map(int,input().split())
#     if x>0 and y>0 :
#         q1+=1
#     elif x<0 and y<0 :
#         q3+=1
#     elif x<0 and y>0 : 
#         q2+=1
#     elif x>0 and y<0 :
#         q4 += 1
#     else :
#         axis +=1 
# print(f"Q1: {q1} \nQ2: {q2} \nQ3: {q3} \nQ4: {q4} \nAXIS: {axis}")

#9506 : ㅇㅑㄱ ㅅㅜ드ㄹㅢ 합  
# while True :
#     m = int(input())
#     if m== -1 :
#         break 
#     arr=[] #약수 리스트 선언 
#     for i in range(1,m):
#         if m%i == 0:
#             arr.append(i) # i 추가하기 리스트에 
#     if sum(arr)==m:
#         print(m," = "," + ".join(str(i) for i in arr), sep="")
#     else :
#         print(m,"is Not perfect")

#10162 : 전자레인지
# time = int(input())
# if time%10:
#     print(-1)
# else:
#     A = B = C = 0
#     A = time//300
#     B = (time%300) // 60
#     C = (time%300) % 60 // 10
#     print(A, B, C)

# #2558 : A + B - 2
# a = int(input())
# b = int(input())
# print(a+b)

#10103 : 주사위 게임 
# round = int(input())
# mScore=100; nScore = 100 
# for _ in range(1,round+1):
#     m, n = map(int,input().split())
#     if m>n :
#         nScore-=m
#     elif m<n :
#         mScore-=n
# print(mScore)
# print(nScore)

# 10214 : BaseBall 
# T = int(input())
# y = 0 ; k =0 
# for _ in range(T):
#     for __ in range(9):
#         m,n = map(int,input().split())
#         y+=m ; k+=n 
#     if y>k :
#         print("Yonsei")
#     elif k>y :
#         print("Korea")
#     else :
#         print("Draw")

# 11557 : 양조장의 해 
# T = int(input())
# for __ in range(T):
#     dictionary = {}
#     maxA = 0 
#     numSchool = int(input()) 
#     for i in range(numSchool):
#         a, b = input().split()
#         dictionary[int(b)] = a
#     for j in dictionary.keys():
#         if maxA<j :
#             maxA = j
#     print(dictionary[maxA]) 

# import math 
# a,b = map(int,input().split())
# print(math.gcd(a,b)) #최대공약수 
# print(a*b//math.gcd(a,b) ) #최소공배수

#최소공배수 
# lcm = a*b// math.gcd(a,b) 
# #최소공배수 = 두 수 곱하기 나누기 두수 최대공약수 
# 세 수 곱하기 나누기 세 수 최대공약수...?

# jaesan = 1000
# count = 0
# array = [500,100,50,10,5,1]

# money = int(input())
# jaesan -= money
# for coin in array:
#     count += jaesan // coin 
#     jaesan %= coin 
# print(count)

#1463 
# 3으로 나눈다 -> 2로 나눈다 -> 1뺀다 
# 3  나눠서 나머지가 0이 아니면 2로 나누는데 나머지가 0이 아니면 1뺀다
# 무한반복 1이 될때 가지 
# .. 10일때 옝하 발생 
# 각 인덱스 값에 1로 만들 수 있는 값을 저장한다
#  필요할때 꺼내 쓴다 
# Dp = dynamic Programming 
# num = int(input())
# arr = [0,0]

# for i in range(2,num+1):
#     #arr[2]부터 2를 나누는것이니깐 1의 값을 가진다 
#     # arr[i] = arr[i-1]+1 #1빼기를 선택했을 때의 경우의 수 
#      arr.append(arr[i-1]+1)
#     if i%3 == 0:
#         arr[i] = min(arr[i],arr[i//3]+1)
#     if i%2 == 0:
#         arr[i] = min(arr[i],arr[i//2]+1)
# print(arr[num])

#11047
# n,k = map(int,input().split())
# count = 0 
# values = [0]*n

# for i in range(n):
#     values[i] = int(input())

# values.sort(reverse = True)
# for coin in values:
#     count += k // coin 
#     k %= coin 
# print(count)

#최 대 
# data = input()
# sum = int(data[0]) #change string to number 
# for i in range(1,len(data)):
#     num = int(data[i])
#     if num <=1 or sum <=1 :
#         sum += num 
#     else :
#         sum *= num 
# print(sum)

# 모험가 길 드  
# n = int(input())
# data = list(map(int,input().split()))
# data.sort()

# result = 0 
# cnt = 0 

# for i in data :
#     cnt +=1 
#     if cnt>=i :
#         result+=1
#         cnt  =0 

# print(result)

# 11399 : ATM 

# n = int(input()) #총 사람의 수 입력 받기 
# arr = list(map(int,input().split())) #시간 입력 받기 
# total = 0 # 총 합 시간 
# personalTime = 0 #매번 갱신되는 개인의 시간 
# arr.sort() #시간 낮은 대로 정렬 

# for time in arr:
#     personalTime+=time 
#     total+=personalTime
# print(total)    

#1541 : 잃어버린 괄호 
# arr = input().split('-')
# firstIndexSum =0
# minusSum = 0

# #첫번째 요소 합구함 
# for i in arr[0].split('+'):
#     firstIndexSum += int(i)

# #이후 마이너스 요소들 합구해서 빼줘야함 
# for piece in arr[1:]:
#     for splits in piece.split('+') :
#         minusSum+=int(splits) 

# print(firstIndexSum-minusSum)

#13305 : 주유소 
# city = int(input())
# length = list(map(int,input().split())) # 길이 
# value = list(map(int,input().split())) #마지막 도시 가격 상관 x 
# sum = 0

# minVal = value[0]

# for i in range(city-1):
#     if(value[i]<minVal):
#         minVal = value[i]
#     sum += length[i]*minVal

# print(sum)
    
#2217 : 로프 
# num = int(input())
# arr=[0]*num 
# for i in range(num):
#     arr[i]=int(input()) 


# #arr 정렬 
# arr.sort(reverse=True) #내림차순 
# for i in range(num):
#     arr[i] = arr[i]*(i+1)

# print(max(arr))

# 2164 : 카드 2
# import sys 
# from collections import deque # 덱 불러오기 
# num = int(sys.stdin.readline())
# queue = deque() 

# for i in range(num):
#     queue.append(i+1)

# while len(queue)!=1:
#     temp = queue.popleft() #왼쪽 반환 및 제거 
#     print(temp, end=" ")
#     queue.append(queue.popleft())


# print(queue.pop()) # 오른쪽 반환 및 제거 

#11866
# import sys 

# n,k = map(int,sys.stdin.readline().split()) # n,k 입력받기 
# arr = [i for i in range(1,n+1)]

# ppl = []
# idx = 0 

# for i in range(n):
#     idx += k-1
#     if(idx>=len(arr)):
#         idx = idx%len(arr)

#     ppl.append(str(arr.pop(idx)))

# print("<",", ".join(ppl),">",sep="")

#10866
# import sys 
# from collections import deque
# test = int(sys.stdin.readline())

# queue = deque()

# def empty():
#     if len(queue)==0:
#         return 1
#     else :
#         return 0 

# for _ in range(test):
#     wn = list(sys.stdin.readline().split())
#     if wn[0] == 'push_front':
#         queue.appendleft(wn[1])
#     elif wn[0] =='push_back':
#         queue.append(wn[1])
#     elif wn[0] == 'pop_front':
#         if(empty()):
#             print("-1")
#         else :
#             print(queue.popleft())
#     elif wn[0] == 'pop_back':
#         if(empty()):
#             print("-1")
#         else :
#             print(queue.pop())
#     elif wn[0] == 'size':
#         print(len(queue))
#     elif wn[0] == 'empty':
#         if(empty()):
#             print("1")
#         else :
#             print("0")
#     elif wn[0] == 'front':
#         if(empty()):
#             print("-1")
#         else :
#             print(queue[0])
#     elif wn[0] == 'back':
#         if(empty()):
#             print("-1")
#         else :
#             print(queue[-1])
#dequeue

# n,k = map(int,input().split())
# arr = list(map(int,input().split()))
# arr.sort()
# print(arr[k-1])


#에라토스테네스의 체 
# n = 1000
# a = [False,False]+[True]*(n-1)
# primes = [] #소수배열 

# for i in range(2,n+1):
#     if a[i]:
#         primes.append(i)
#         for j in range(2*i,n+1,i): #2+i부터 n+1까지 i간격 
#             a[j] = False 
# print(primes)

# print(str(100))
# print(str(100)[::-1])

# 1747 : 소수&팰린드롬 

# import math 

# #prime func
# def primeNumber(x):
#     for i in range(2,int(math.sqrt(x))+1):
#         if x % i ==0:
#             return False 
#     return True #소수당 

# n = int(input())

# max = 1000001 
# cnt =0 

# for i in range(n,max):
#     if i == 1:
#         continue
#     if str(i)==str(i)[::-1]: #펠
#         if primeNumber(i) :
#             cnt = i 
#             break 

# if cnt == 0 :
#     cnt = 1003001 
# print(cnt)

# 1652 :누울 자리를 찾아라 
# n = int(input())

# space_w = 0 ; total_w=0
# space_h = 0 ; total_h =0

# arr = []
# for _ in range(n):
#     arr.append(input())

# #가로 눕기 가능한 수 구하기 
# for i in arr:
#     for j in i: #가로 한 줄 체크 
#         if j=='.':
#             space_w +=1
#         else :
#             if space_w>1:
#                 total_w+=1
#             space_w = 0 # 초기화 
#     #전부 .일경우 
#     if space_w>1:
#         total_w+=1
#     space_w=0 #초기화 

# # #세로 눕기 가능한 수 구하기 

# for i in range(n):
#     for j in range(n):
#         if arr[j][i]=='.':
#             space_h+=1
#         else :
#             if space_h>1:
#                 total_h+=1
#             space_h=0 
#     if space_h>1:
#         total_h+=1
#     space_h=0 

# print(total_w,end=" ") #가로 눕기 
# print(total_h) #세로 눕기

#2621
# import sys  

# numArr=[0]*10
# r=0;b=0;y=0;g=0


# for i in range(5):
#     arr = list(sys.stdin.readline().split())
#     numArr[int(arr[1])]+=1 
#     if arr[0]=='B':
#         b+=1
#     elif arr[0]=='R':
#         r+=1
#     elif arr[0]=='Y':
#         y+=1
#     else : #green 
#         g+=1

# print(r,b,y,g)
# print(numArr)
# #조건1
# if(b==5 or r==5 or y==5 or g ==5):
#     print(max(numArr)+900)

# #조건1 

# 8979 : 올림픽 
# import sys 
# input = sys.stdin.readline

# n,k = map(int,input().split())
# arr=[]

# for i in range(n):
#     arr.append(list(map(int,input().split())))


# print(arr)
# #################
# arr.sort(key = lambda x :(-x[1],-x[2],-x[3])) #내림차순 정렬 
# print(arr)

# for i in range(n):
#     if arr[i][0] == k:
#         idx = i 

# # #공동등수가 될 수 있으므로 
# for i in range(n):
#     if arr[i][1:] == arr[idx][1:]: #메달 같은데 더 앞에 있는거 ! = 등수 땡겨 ! 
#         print(i+1)
#         break 


#2816 : 디지털티비 

# from os import remove

# num = int(input())
# ch = []
# for i in range(num):
#     ch.append(input()) #채널입력받기
     
# kbs1Idx=ch.index('KBS1')
# ch.remove('KBS1')
# kbs2Idx=ch.index('KBS2')

# #KBS1 이 KBS2보다 아래 
# #KBS1이 아래로 올것이니깐 ! 
# # if kbs1Idx>kbs2Idx:
#     # kbs2Idx+=1 

# #kbs1 Idx => 0으로 
# #kbs2 Idx => 1로 
# print('1'*kbs1Idx + '4'*kbs1Idx + '1'+'1'*kbs2Idx+'4'*kbs2Idx)

#2621:카드게임 
# allCard={} #dict #카드

# num_cnt =[0 for _ in range(10)] #빈도 

# nums = set() #save number

# for _ in range(5):
#     color,num =input().split()
#     if color in allCard:
#         allCard[color].append(int(num))
#     else :
#         allCard[color] = [int(num)]

#     num_cnt[int(num)] +=1 #카드 카운트
#     nums.add(int(num)) #set => 집합 => 중복되는 숫자 저장x

# nums=sorted(list(nums)) #set -> list로 전환 



# #같은색깔 
# def all_same_color(allCard):
#     #딕셔너리는 벨류값에 따라 길이가 정해진다. 
#     if len(allCard)==1:
#         return True
#     else :
#         return False 


# #연속체크 
# def continue_num(num_cnt):
#     idx=0
#     for i in range(1,10):
#         if num_cnt[i] != 1:
#             if num_cnt[i] !=0:
#                 #2번이상 
#                 return False 
#         else:
#             if idx==0:
#                 idx = i 
#             else : #이미 인덱스 하나 들어옴 
#                 if idx+1 != i: #연속쫑 
#                     return False 
#                 else :
#                     idx = i #idx값 초기화
#     return True 

# #같은숫자
# def cnt_same_num(num_cnt):
#     cnts = sorted(num_cnt, reverse=True)
#     if cnts[0]==4: #4장같은 숫자
#         return 8
#     elif cnts[0]==3:
#         if cnts[1]==2:
#             return 7 #3장,2장같은 숫자 
#         else:
#             return 4 #3장만 같은 숫자 
#     elif cnts[0]==2:
#         if cnts[1]==2: 
#             return 3 #2,2
#         else :
#             return 2 #2

# #nums = 제일큰숫자
# res = 100 + nums[-1] # condition 9
# if all_same_color(allCard):
#     if continue_num(num_cnt):
#         res = max(res,900+nums[-1])  # condition 1
#     else : 
#         res = max(res,600+nums[-1]) # condition 4 
# else :
#     if continue_num(num_cnt): #condition 5 
#         res = max(res,500+nums[-1])

# cnt_same_num = cnt_same_num(num_cnt)
# if cnt_same_num == 8:
#     res = max(res,800+num_cnt.index(4)) # condition 2
# elif cnt_same_num == 7:
#     res = max(res,700+10*num_cnt.index(3)+num_cnt.index(2)) #3,2장같은거, condition 3
# elif cnt_same_num == 4:
#     res = max(res,400+num_cnt.index(3)) # condition 6
# elif cnt_same_num == 3:
#     idx1 = num_cnt.index(2)
#     idx2 = num_cnt.index(2,idx1+1,10)
#     res = max(res,300+10*idx2+idx1) # condition 7
# elif cnt_same_num == 2:
#     res = max(res,200+num_cnt.index(2)) #condition 9

# print(res)


#11764 : 연결요소
# import sys

# sys.setrecursionlimit(10**6) #python 의 재귀 깊이 제한은 1000으로 매우 얕으므로 재귀 한계 설정은 선택이 아닌 필수 
# input = sys.stdin.readline

# n,m = map(int,input().split())

# visited=[0 for _ in range(n+1)]


# def DFS(start):
#     visited[start] = 1
#     for k in range(1,n+1):
#         if 
#DFS -> Stack
# 
# import sys 
# import operator as op 
# from functools import reduce

# def nCk(n,k):
#     k = min(k,n-k)
#     numerator = reduce(op.mul,range(n,n-k,-1),1)
#     denominator = reduce(op.mul,range(1,k+1),1)
#     return numerator//denominator


# input = sys.stdin.readline
# n,k = map(int,input().split())

# com = nCk(n,k)
# print(com%1000000007)


# 1629 : 곱셈 
# import sys
# input = sys.stdin.readline

# a,b,c = map(int,input().split())

# def divCon(a,b):
#     if b==1:
#         return a%c 
#     else:
#         div = divCon(a,b//2)

#         if b%2==0: #짝수 
#             return div*div%c 
#         else : #홀수 
#             return div*div*a%c 

# print(divCon(a,b))

# 1140 : 이항계수 3

# #제곱 분할정복 함수 
# def divCon(a,b):
#     if b==1:
#         return a%p
#     else:
#         div = divCon(a,b//2)

#         if b%2==0: #짝수 
#             return div*div%p
#         else : #홀수 
#             return div*div*a%p

# n,k = map(int,input().split())
# p = 1000000007

# fact = [1 for _ in range(n+1)]
# #factorial 계산 
# for i in range(2,n+1):
#     fact[i]=fact[i-1]*i%p

# A = fact[n]
# B = fact[n-k]*fact[k]%p 

# print((A%p)*(divCon(B,p-2)%p)%p)

# 11051 : 이항계수 2

#제곱 분할정복 함수 
# def divCon(a,b):
#     if b==1:
#         return a%p
#     else:
#         div = divCon(a,b//2)

#         if b%2==0: #짝수 
#             return div*div%p
#         else : #홀수 
#             return div*div*a%p

# n,k = map(int,input().split())
# p = 10007

# fact = [1 for _ in range(n+1)]
# #factorial 계산 
# for i in range(2,n+1):
#     fact[i]=fact[i-1]*i%p

# A = fact[n]
# B = fact[n-k]*fact[k]%p 

# print((A%p)*(divCon(B,p-2)%p)%p)

#2749 : 피보 3 
# mod = 1000000
# p = mod // 10*15

# num = int(input())

# pivo =[0,1]

# for i in range(2,p):
#     pivo.append(pivo[i-1]+pivo[i-2]) ##피보
#     pivo[i] %=mod 
# print(pivo[])

#10826 : 피보 4,1,2,5

# num = int(input())

# pivo =[0,1]

# for i in range(2,num+1):
#     pivo.append(pivo[i-1]+pivo[i-2]) ##피보
# print(pivo[num])

#11724 : 연결 요소의 개수
# 
# #######dfs  
# import sys 
# sys.setrecursionlimit(10**6) #깊이제한 늘리기 
# input = sys.stdin.readline

# def dfs(v):
#     visited[v]=1

#     for i in range(1,n+1):
#         if visited[i]==0 and graph[v][i]==1:
#             dfs(i)


# n,m = map(int,input().split()) #n,m 입력 
# graph = [[0]*(n+1) for _ in range(n+1)]
# visited =[0 for _ in range(n+1)]
# cnt =0

# for i in range(m):
#     u,v = map(int,input().split())
#     graph[u][v]=1
#     graph[v][u]=1

# for i in range(1,n+1):
#     if visited[i]!=1:
#         dfs(i)
#         cnt+=1

# print(cnt)

####bfs 
# import sys 
# from collections import deque
# sys.setrecursionlimit(10**6) #깊이제한 늘리기 
# input = sys.stdin.readline

# def bfs(v):
#     queue =deque()
#     queue.append(v)
#     visited[v]=1
#     while(queue):
#         v = queue[0]
#         queue.popleft()

#         for i in range(1,n+1):
#             if visited[i]==0 and graph[v][i]==1:
#                 queue.append(i)
#                 visited[i]=1


# n,m = map(int,input().split()) #n,m 입력 
# graph = [[0]*(n+1) for _ in range(n+1)]
# visited =[0 for _ in range(n+1)]
# cnt =0

# for i in range(m):
#     u,v = map(int,input().split())
#     graph[u][v]=1
#     graph[v][u]=1

# for i in range(1,n+1):
#     if visited[i]!=1:
#         bfs(i)
#         cnt+=1

# print(cnt)


#1260 :DFS BFS 
# from collections import deque
# import sys 
# input = sys.stdin.readline

# def dfs(v):
#     print(v,end=' ')
#     visited[v]=1

#     for i in range(1,n+1):
#         if visited[i]==0 and matrix[v][i]==1:
#             dfs(i)

# def bfs(v):
#     queue =deque()
#     queue.append(v)
#     visited[v]=0
#     while(queue):
#         v = queue[0]
#         print(queue.popleft(),end=' ')

#         for i in range(1,n+1):
#             if visited[i]==1 and matrix[v][i]==1:
#                 queue.append(i)
#                 visited[i]=0


# n,m,v = map(int,input().split())
# matrix = [[0]*(n+1) for _ in range(n+1)] #인접행렬 생성
# visited = [0 for _ in range(n+1)]

# for i in range(m):
#     x,y = map(int,input().split())
#     matrix[x][y]=1
#     matrix[y][x]=1

# dfs(v)
# print()
# bfs(v)

#2606 : 바이러스 
#######dfs  
# import sys 
# input = sys.stdin.readline

# def dfs(v):
#     global cnt
#     visited[v]=1
#     for i in range(1,n+1):
#         if visited[i]==0 and graph[v][i]==1:
#             dfs(i)
#             cnt+=1 #1번


# n = int(input()) # computer 
# m = int(input()) # network 

# graph = [[0]*(n+1) for _ in range(n+1)]
# visited =[0 for _ in range(n+1)]
# cnt =0

# #컴터연결 
# for i in range(m):
#     u,v = map(int,input().split())
#     graph[u][v]=1
#     graph[v][u]=1

# dfs(1)

# print(cnt)

#1012 : 유기농 배추 
# import sys 
# input = sys.stdin.readline
# sys.setrecursionlimit(10**4)


# # def bfs(x,y):
# #     queue =[[x,y]]
# #     while queue:
# #         a,b = queue[0][0],queue[0][1]
# #         del queue[0]
# #         for i in range(4):
# #             cx = a+dx[i]
# #             cy = b+dy[i]
# #             if 0<=cx<n  and 0<=cy<m and graph[cx][cy]==1:
# #                 graph[cx][cy]=0
# #                 queue.append([cx,cy])

# def dfs(x,y):
#     graph[x][y]=0
#     for i in range(4):
#         cx = x+dx[i]
#         cy = y+dy[i]
#         if 0<=cx<n  and 0<=cy<m and graph[cx][cy]==1: #방문안한 곳 
#             dfs(cx,cy)

# test = int(input()) # computer 

# #방향벡터 
# dx = [1,-1,0,0]
# dy = [0,0,-1,1]


# for _ in range(test):
#     # n:세로 m:가로
#     m,n,k= map(int,input().split())
#     graph = [[0]*m for _ in range(n)]
#     cnt=0 #지렁지렁 
    
#     #배추
#     for i in range(k):
#         a,b = map(int,input().split())
#         graph[b][a]=1
#     for j in range(n):
#         for k in range(m):
#             if graph[j][k]==1:
#                 dfs(j,k)
#                 cnt+=1
#     print(cnt)

# import sys 
# input=sys.stdin.readline

# n = int(input())
# arr = input().split()
# strA = ''.join(arr)

# m = int(input())

# for _ in range(m):
#     idx1,idx2=map(int,input().split())
#     strNum = strA[idx1-1:idx2]
#     if strNum==strNum[::-1]:
#         print(1)
#     else:
#         print(0)

# #펠린?
# import sys 
# input=sys.stdin.readline

# n = int(input())
# arr = list(input().split())
# m = int(input())

# dp = [[0 for _ in range(n)]for _ in range(n)]

# for i in range(n):
#     dp[i][i] = 1 #길이 1 전부 펠린 

# for i in range(n-1): 
#     if arr[i]==arr[i+1]:#길이 2인데 같은 숫자 펠린 
#         dp[i][i+1]=1 
# for i in range(2,n):
#     for j in range(n-i):
#         if arr[j] == arr[i+j] and dp[j+1][i+j-1]==1:
#             dp[j][i+j]=1

# for i in range(m):
#     idx1,idx2 = map(int,input().split())
#     print(dp[idx1-1][idx2-1])

#10815 : 숫자카드
# def bs(target,data):
#     data.sort()
#     start = 0
#     end = len(data)-1

#     while start<=end:
#         mid = (start+end)//2 

#         if data[mid] == target:
#             print(1,end=' ')
#             return 1
#         elif data[mid]<target:
#             start = mid + 1 
#         else :
#             end = mid -1 
#     return None 


#10813
# import sys 
# sys.setrecursionlimit(10**9)

# def bsr(target,start,end,data):
#     if start>end :
#         return None 
#     mid = (start+end)//2
#     if data[mid]==target:
#         return 1
#     elif data[mid]>target:
#         end = mid -1
#     else:
#         start = mid + 1
#     return bsr(target,start,end,data)

# n = int(input())
# arr1 = list(map(int,input().split()))
# m = int(input())
# arr2 = list(map(int,input().split()))

# arr1.sort()
# for i in range(m):
#     if bsr(arr2[i],0,n,arr1):
#         print(1,end=' ')
#     else : 
#         print(0,end=' ')

#:1920
# import sys 
# sys.setrecursionlimit(10**6)

# def bsr(target,start,end,data):
#     if start>end :
#         return None 
#     mid = (start+end)//2
#     if data[mid]==target:
#         return 1
#     elif data[mid]>target:
#         end = mid -1
#     else:
#         start = mid + 1
#     return bsr(target,start,end,data)

# n = int(input())
# arr1 = list(map(int,input().split()))
# m = int(input())
# arr2 = list(map(int,input().split()))

# arr1.sort()
# for i in range(m):
#     if bsr(arr2[i],0,n-1,arr1):
#         print(1)
#     else : 
#         print(0)

#1016
# import sys
# input = sys.stdin.readline

# def prime_list(MIN,MAX):
#     `answer` = MAX-MIN+1 
#     check = [False]*(MAX-MIN+1)
#     i=2 
#     while i*i <= MAX: 
#         square_number = i*i 
#         remain = 0 if MIN%square_number==0 else 1 
#         j = MIN//square_number + remain
#         while square_number*j <= MAX: 
#             if not check[square_number*j-MIN]:
#                  check[square_number*j-MIN]=True 
#                  answer-=1 
#             j+=1
#         i+=1 
#     print(answer)

# m,n = map(int,input().split())
# prime_list(m,n)

#영역구하기 : 2583
# import sys 
# sys.setrecursionlimit(10**6)
# input = sys.stdin.readline
# #m 세로 n가로 
# m,n,k = map(int,input().split())
# graph = [[0]*n for _ in range(m)]
# cnt = 0

# dx = [1,-1,0,0]
# dy = [0,0,-1,1]
# wide =1

# total =[]

# def dfs(x,y):
#     global wide #초기 넓이 
#     graph[x][y]=1 #방문 ! 
#     for i in range(4):
#         cx = x+dx[i]
#         cy = y+dy[i]
#         if 0<=cx<m  and 0<=cy<n and graph[cx][cy]==0: #방문안한 곳 
#             dfs(cx,cy)
#             wide+=1 #넓이 올라가랏 
    

# for _ in range(k): #사각형 색칠 
#     x1,y1,x2,y2 = map(int,input().split())
#     for j in range(y1,y2):
#         for i in range(x1,x2):
#             graph[j][i]=1 #색칠 

# for j in range(m):
#     for k in range(n):
#         if graph[j][k]==0:
#             dfs(j,k)
#             total.append(wide)
#             cnt+=1
#             wide=1 #제일 첫 넓이는 1
    
# total.sort()

# print(cnt)
# for totals in total:
#     print(totals,end=" ")lsdlfasljd

#10026 : 적록색약 
# import sys
# sys.setrecursionlimit(10**6)
# input=sys.stdin.readline

# n = int(input())
# dx = [1,-1,0,0]
# dy = [0,0,-1,1]
# cnt1=0;cnt2=0;cnt3=0;cnt4=0
# flag =0

# def dfsG(x,y): 
#     graphfdafdkfldskf[x][y]='Rr' #방문 ! 
#     for i in range(4):
#         cx = x+dx[i]
#         cy = y+dy[i]
#         if 0<=cx<n  and 0<=cy<n and graph[cx][cy]=='G': #방문안한 곳 
#             dfsG(cx,cy)

# def dfsR(x,y): 
#     flag = graph[x][y]
     
#     for i in range(4):
#         cx = x+dx[i]
#         cy = y+dy[i]
#         if(flag=='R'):
#             graph[x][y]='Rr' #방문 !
#             if 0<=cx<n  and 0<=cy<n and graph[cx][cy]=='R': #방문안한 곳 
#                 dfsR(cx,cy)
#         elif(flag=='B'):
#             graph[x][y]='B.' #방문 !         
#             if 0<=cx<n  and 0<=cy<n and graph[cx][cy]=='B': #방문안한 곳 
#                 dfsR(cx,cy)
#         elif(flag=='G'):
#             graph[x][y]='Rr' #방문 ! 
#             if 0<=cx<n  and 0<=cy<n and graph[cx][cy]=='G': #방문안한 곳 
#                 dfsR(cx,cy)

# # def dfsB(x,y): 
# #     graph[x][y]='B.' #방문 ! 
# #     for i in range(4):
# #         cx = x+dx[i]
# #         cy = y+dy[i]
# #         if 0<=cx<n  and 0<=cy<n and graph[cx][cy]=='B': #방문안한 곳 
# #             dfsB(cx,cy)

# def dfsRr(x,y):
#     graph[x][y]=1 #방문 ! 
#     for i in range(4):
#         cx = x+dx[i]
#         cy = y+dy[i]
#         if 0<=cx<n  and 0<=cy<n and graph[cx][cy]=='Rr': #방문안한 곳 
#             dfsRr(cx,cy)


# graph = [0 for _ in range(n)]

# for i in range(n):
#     line = input()
#     graph[i] =list(line) #문자열 넣기 

# #적록색약아니면 R G B 따로 
# #적록색약이면 R B => 빨간색 초록색 색상 구분 불가 

# for j in range(n):
#     for k in range(n):
#         if (graph[j][k]=='R'):
#             dfsR(j,k)
#             cnt1+=1
#         elif (graph[j][k]=='G'):
#             dfsR(j,k)
#             cnt2+=1
#         elif (graph[j][k]=='B'):
#             dfsR(j,k)
#             cnt3+=1

# for j in range(n):
#     for k in range(n):
#         if (graph[j][k]=='Rr'):
#             dfsRr(j,k)
#             cnt4+=1
 
# print(cnt1+cnt2+cnt3, cnt3+cnt4)

#2667 : 단지번호 붙이기 
# import sys
# sys.setrecursionlimit(10**6)
# input=sys.stdin.readline

# cnt=0;total=1

# dx = [1,-1,0,0]
# dy = [0,0,-1,1]
# apt=[]

# def dfs(x,y):
#   global total
#   graph[x][y]=0 #방문 ! 
#   for i in range(4):
#       cx = x+dx[i]
#       cy = y+dy[i]
#       if 0<=cx<n  and 0<=cy<n and graph[cx][cy]==1:
#         total+=1
#         dfs(cx,cy)

# n = int(input())
# graph = []
# for i in range(n):
#     graph.append(list(map(int, input().rstrip())))


# for j in range(n):
#     for k in range(n):
#         if (graph[j][k]==1):
#             dfs(j,k)
#             cnt+=1
#             apt.append(total)
#             total=1

# apt.sort()
# print(cnt) #총집 
# for i in range(cnt):
#   print(apt[i])

# n,m = map(int,input().split())
# n = int(input())
# m = int(input())

# total = 0 ; avg = 0 #총점, 평균 
# arr = [[0]*m for _ in range(n)]
# print(arr)
# print("1.국어 2.수학, 3.영어 순으로 입력해주세요 !")

# #학생별로 
# for i in range(m):
#     print(f"{i+1}번째 학생")
#     for j in range(n):
#         print(f"{j+1}반째 과목")
#         arr[i][j] = int(input())

# print(arr)


# 수빈
# import sys
# from collections import deque
# input=sys.stdin.readline

# queue = deque()
# n,k = map(int,input().split())

# def bfs():
#     queue.append(n)
#     while(queue):
#         soobin = queue.popleft() #수빈이 위치 저장 
#         if(soobin==k):
#             print(sec[soobin])
#             break
#         for walk in (soobin-1,soobin+1,soobin*2):
#             if (0<=walk<MAX and  sec[walk]==0 ):
#                 sec[walk] = sec[soobin]+1
#                 queue.append(walk)
#                 #5는 어쩔수 없이 한번 오게된당.. 
        

# MAX = 100001
# sec = [0] * MAX #초 리스트 
# bfs()


#7576 : 토마토 
# import sys
# input = sys.stdin.readline
# from collections import deque #BFS

# m,n = map(int,input().split())

# dx = [1,-1,0,0]
# dy = [0,0,-1,1]

# queue = deque()
# graph=[]

# for i in range(n):
#     graph.append(list(map(int, input().rstrip().split())))

# #붙이기 

# #익은토마토 조사 
# for i in range(n):
#     for j in range(m):
#         if graph[i][j]==1:
#             queue.append([i,j])

# def bfs():
#   while queue:
#       a,b = queue.popleft() #i.j삽입 
#       for i in range(4):
#           cx = a+dx[i]
#           cy = b+dy[i]
#           if 0<=cx<n  and 0<=cy<m and graph[cx][cy]==0: 
#               graph[cx][cy] = graph[a][b] + 1 #시간 더해나감 
#               queue.append([cx,cy])
# # print(graph)
# bfs()
# flag = 1 # 1 익음 0 안익음  
# time = -2 
# # print(graph)
# for j in graph:
#     for k in j:
#         if k==0: #익지 않은것이 존재 
#             flag =0 #안익음... 
#         time =max(time,k)

# if time == 1 : #최댓값이 1 #다익음   
#     print(0)
# elif flag ==0: #안익은게 있음/// 
#     print(-1)
# else :
#     print(time - 1) #1초부터 시작하니 1빼줌 

#4963 : 섬의갯수 
# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10**)

# dx = [1,-1,0,0,1,1,-1,-1]
# dy = [0,0,-1,1,1,-1,1,-1] #대각선 벡터도 추가 

# def dfs(x,y):
#   graph[x][y]=0 #방문 ! 
#   for i in range(8):
#       cx = x+dx[i]
#       cy = y+dy[i]
#       if 0<=cx<n  and 0<=cy<m and graph[cx][cy]==1:
#         dfs(cx,cy)

# while True :
#     cnt=0
#     m,n = map(int,input().split())
#     if(m==n==0):
#         break
#     graph=[]

#     for i in range(n):
#         graph.append(list(map(int, input().rstrip().split()))) #입력받기 

#     for j in range(n):
#         for k in range(m):
#             if (graph[j][k]==1):
#                 dfs(j,k)
#                 cnt+=1
#     print(cnt)    


#2718 : 미로탐색 
# import sys
# input = sys.stdin.readline
# from collections import deque #BFS

# m,n = map(int,input().split())

# dx = [1,-1,0,0]
# dy = [0,0,-1,1]

# queue = deque() #칸수저장 
# graph=[]

# for i in range(m):
#     graph.append(list(map(int, input().rstrip()))) 

# #붙이기 

# queue.append([0,0]) #0,0에서 출발 

# def bfs():
#   while queue:
#       a,b = queue.popleft() #i.j삽입 
#       for i in range(4):
#           cx = a+dx[i]
#           cy = b+dy[i]
#           if 0<=cx<m  and 0<=cy<n and graph[cx][cy]==1: 
#               graph[cx][cy] = graph[a][b] + 1 #칸수 더해나감 
#               queue.append([cx,cy])
# bfs()

# print(graph[m-1][n-1])

#7562 : 나이트 
# import sys
# input = sys.stdin.readline
# from collections import deque #BFS

# # 나이트 8가지 케이스 
# dx = [1,2,1,2,-1,-1,-2,-2]
# dy = [2,1,-2,-1,2,-2,1,-1]

# def bfs():
#   while queue:
#       a,b = queue.popleft() #i.j삽입 
#       for i in range(8):
#           cx = a+dx[i]
#           cy = b+dy[i]
#           if 0<=cx<n  and 0<=cy<n and graph[cx][cy]==0: #아직한번도 안간곳
#               graph[cx][cy] = graph[a][b] + 1 #칸수 더해나감 
#               queue.append([cx,cy])

# test = int(input())
# for _ in range(test):

#     # 덱선언
#     queue = deque()

#     n = int(input())
#     graph = [[0] * n for _ in range(n)] #그래프 생성

    # knight_x, knight_y = map(int,input().split()) #나이트 x,y값 
    # dochak_x, dochak_y = map(int,input().split())

#     queue.append([knight_x,knight_y])
#     bfs()
#     graph[knight_x][knight_y]=0
#     print(graph[dochak_x][dochak_y])

#2589 : 보물섬
# import sys 
# input = sys.stdin.readline
# from collections import deque #BFS


# dx = [1,-1,0,0]
# dy = [0,0,-1,1]

# def bfs(x,y):
#     queue.append([x,y])
#     timeGraph =[[0]*m for _ in range(n)] #임시그래프 생성 
#     timeGraph[x][y]=1 #시간을위한 그래프
#     time =0
#     while queue:
#       x,y = queue.popleft() #i.j삽입
#       for i in range(4):
#           cx = x+dx[i]
#           cy = y+dy[i]
#           if 0<=cx<n  and 0<=cy<m :
#               if graph[cx][cy] == 'L' and timeGraph[cx][cy]==0: #아직탐색안한 육지
#                   timeGraph[cx][cy] = timeGraph[x][y] + 1 #시간 더해나감 
#                   time = max(time,timeGraph[cx][cy])
#                   queue.append([cx,cy])
#     return time-1 #있던자리빼기 

# queue = deque()
# n,m = map(int,input().split()) #세로,가로 
# graph = [list(input().rstrip()) for _ in range(n)] #그래프 입력받기 
# cnt = 0 

# for i in range(n):
#     for j in range(m):
#         if graph[i][j] == 'L': #L이 저장된곳에 cnt 최댓값 출력 
#             cnt=max(cnt,bfs(i,j)) 
# print(cnt)

# import sys
# input=sys.stdin.readline


# l,c = map(int,input().split()) # 순열 c C l 
# visited = [0 for _ in range(c)]
# arr2=[] #순열저장 
# def dfs(cnt,idx):
#     if cnt== l: #l만큼의 단어 
#         mo = 0 #모음 
#         ja = 0 #자음 
#         for i in range(l):
#             if arr2[i] in 'aeiou': 
#                 mo+=1
#             else :
#                 ja +=1 
#         if mo>=1 and ja>=2: #조건만족 
#             print(''.join(arr2)) #리스트 출력 
#         return 
#     for i in range(idx,c):
#         if visited[i]==0:
#             arr2.append(arr[i])
#             visited[i]=1 #방문 
#             dfs(cnt+1,i+1)
#             visited[i]=0
#             # print(arr2[-1])
#             del arr2[-1] #마지막부분지우기 


# arr = input().split() #c만큼 리스트 입력받기 
# arr.sort() #알파벳순으로 정렬 

# dfs(0,0)

# korea = int(input("국어 점수를 입력하세요."))
# math = int(input("수학 점수를 입력하세요."))
# english = int(input("영어 점수를 입력하세요."))

# total = korea+math+english
# avg = total/3

# print(f"총점 : {total}")
# print(f"평균 : {round(avg,2)}")


# import math 

# print(""" 
# 본 프로그램은 섭씨를 화씨로 변환해주는 프로그램입니다.
# 변환하고 싶은 섭씨 온도를 입력해주세요 :""",end=" ")
# num1 = float(input()) #섭씨온도
# num1 = (((1.8)*num1))+32


# num1 = round(num1,2)
# num2 = math.ceil(num1)
# num3 = math.floor(num1)
# print(num1,num2,num3)



# c = float(input("섭씨온도를 입력해주세요:"))
# f = ((9/5*c)+32)
# print("화씨온도:",round(f,2))

# tempC = float(input())
# print("섭씨온도 : ", tempC)
# tempF = round((9/5)*tempC+32,2)
# print("화씨온도 : ", tempF)

# print("성적을 입력해주세요 : ",end=" ")
# score = int(input())

# if score>=90 and score<=100 :
#     print("A");
# elif score>=80 and score<90:
#     print("B")
# elif score>=70 and score<80:
#     print("C")
# elif score>=60 and score<70:
#     print("D")    
# else :
#     print("F")

#구구단을 for문을 통해서 작성해보자
#for문을 하나만 사용해서 
# 숫자를 입력받고 그에 해당하는 구구단을 출력하자

# 예시 입력 
# 숫자를 입력하세요 : 3
# 3*1 = 3 
# 3*2= 6... 출력
# for i in range(9):
#     for j in range(9):
#         print(f"{i+1} X {j+1} = {(i+1)*(j+1)}")
#     print()

# -> while 반복문으로 구구단 작성하기 5분
# i=1
# while i<10:
#     j=1
#     while(j<10):
#         print(i,"X",j,i*j)
#         j+=1
#     i+=1

# A,B,C = map(int,input().split())
# print((A+B)%C)
# print(((A%C)+(B%C))%C)
# print((A*B)%C)
# print(((A%C)*(B%C))%C)

# num1 = int(input())
# num2 = int(input())

# print(num1*(num2%10))
# a=num1*(num2%10)
# # num2 = num2/10
# num2= num2//10
# print(num1*(num2%10))
# b=num1*(num2%10)
# num2= num2//10
# print(num1*(num2%10))
# c=num1*(num2%10)
# print(a+b*10+c*100)

#예제 1
# num1,num2 = map(int,input().split())
# print("덧셈 : ",end="")
# print(num1+num2)
# print("뺄셈 : ",end="")
# print(num1-num2)
# print("곱셈 : ",end="")
# print(num1*num2)
# print("나눗셈 : ",end="")
# print(num1//num2)
# print(f"나머지 : {num1%num2}")


# print("본 프로그램은 섭씨를 화씨로로 변환해주는 프로그램입니다  변환하고 싶은 섭씨 온도를 입력해 주세요")
# num = float(input())
# print(f"섭씨온도 : {num}")
# num = (((1.8)*num))+32
# print(f"화씨온도 {num}")



# print("국어 점수를 입력하세요.",end=" ")
# korea = int(input())
# print("수학 점수를 입력하세요.",end=" ")
# math = int(input())
# print("영어 점수를 입력하세요.",end=" ")
# english = int(input())

# total = korea+math+english
# avg = float(total)/3

# if(90<=total<=100):
#     print("A")


# if 90<=avg<=100 :
#     print("A");
# elif avg>=80 and avg<90:
#     print("B")
# elif avg>=70 and avg<80:
#     print("C")
# elif avg>=60 and avg<70:
#     print("D")    
# else :
#     print("F")


# from random import choice


# print(""""
# *****계산기*****
# 1. 덧셈
# 2. 뺄셈
# 3. 곱셈
# 4. 나눗셈
# 5. 나머지 
# 선택하세요.
# """)
# choice= int(input()) 
# num1,num2 = map(int,input().split())
# if(choice==1):
#     print(f"덧셈 : {num1+num2}")
# elif(choice==2):
#     print(f"나머지 : {num1%num2}")
# elif(choice==3):
#     print(f"나머지 : {num1%num2}")
# elif(choice==4):
#     print(f"나머지 : {num1%num2}")
# elif(choice==5):
#     print(f"나머지 : {num1%num2}")
# else:
#     print(f"나머지 : {num1%num2}")



# x= 3*50
# y = x+120
# z = y//3 
# print(z)

# num1 = int(input())
# num2 = int(input())

# num1,num2 = map(int,input().split("@"))
# print(num1+num2)

# a = "dongguk university"
# b = "level"
# print(a[-1])
# print(a[0])
# print(a[:])
# print(a[-10:])
# print(a[-30:30])
# print(b[::2])

# color = ['white','black','blue','apple']
# arr = [4,5,1,2,8]
# color.append("red")
# color.extend(["pink","yellow"])
# color.insert(2,"orange")
# del color[0]
# color.append("blue")
# color.remove("blue")
# color.remove("blue")
# color.sort()
# arr.append(5)
# arr.sort(reverse=True)
# arr.reverse()
# print(arr.count(5))
# print(arr.index(5))
# print(arr)
# print(color)

# num1 =int(input())
# num2= int(input())
# print(num1*(num2%10))
# print(num1*(num2//10%10))
# print(num1*(num2//100))
# print(num1*num2)

# 암호 
# import sys
# input=sys.stdin.readline

# l,c = map(int,input().split()) 

# visited = [0 for _ in range(c)]
# arr2=[] #순열저장 
# def dfs(cnt,idx):
#     if cnt== l: #l만큼의 단어 
#         mo = 0 #모음 
#         ja = 0 #자음 
#         for i in range(l):
#             if arr2[i] in 'aeiou': 
#                 mo+=1
#             else :
#                 ja +=1 
#         if mo>=1 and ja>=2: #조건만족 
#             print(''.join(arr2)) #리스트 출력 
#         return 
#     for i in range(idx,c):
#         if visited[i]==0:
#             arr2.append(arr[i])
#             visited[i]=1 #방문 
#             dfs(cnt+1,i+1)
#             visited[i]=0
#             # print(arr2[-1])
#             del arr2[-1] #마지막부분지우기 

# arr = input().split() #c만큼 리스트 입력받기 
# arr.sort() #알파벳순으로 정렬 

# dfs(0,0)

#2309 : 일곱난쟁이
# import sys
# input=sys.stdin.readline

# visited = [0 for _ in range(9)]
# arr =[0]*9
# arr2=[] #찐 난쟁이


# def dfs(cnt,idx):
#     if cnt== 7: #길이가 7
#         total=0
#         for i in range(7):
#             total+=arr2[i]
#         if total==100:
#             arr2.sort() #정렬의 문제 What..?
#             for i in range(7):
#                 print(arr2[i])
#         return

#     for i in range(idx,9):
#         if visited[i]==0:
#             arr2.append(arr[i])
#             visited[i]=1 #방문 
#             dfs(cnt+1,i+1)
#             visited[i]=0
#             del arr2[-1] #마지막부분지우기 

# for i in range(9):
#     arr[i]=int(input())
# dfs(0,0)

#10819 : 차이를 최대로 
# import sys
# from itertools import permutations #순열 가져오기 
# input=sys.stdin.readline

# m = int(input())
# arr = list(map(int,input().split())) ## 숫자입력시 list선언 필수 

# per = permutations(arr) #순열 리스트 생성 
# MAX = 0 

# for i in per:
#     total = 0
#     for j in range(m-1):
#         total+=abs(i[j]-i[j+1])
#     if total > MAX : #최댓값보다 큼 
#         MAX = total  

# print(MAX)

# #1987 : 알파벳
# import sys
# input=sys.stdin.readline

# cnt=0;total=1

# #방향벡터 
# dx = [1,-1,0,0] 
# dy = [0,0,-1,1]
# visited=[]

# def dfs(x,y,total):
#     global cnt 
#     visited.append(graph[x][y])
#     cnt = max(total,cnt)
#     # print(visited)
#     for i in range(4):
#         cx = x+dx[i]
#         cy = y+dy[i]
#         if 0<=cx<n  and 0<=cy<m:
#             if graph[cx][cy] not in visited: #방문하지 않은 알파벳 
#                 dfs(cx,cy,total+1)
#                 del visited[-1]
    
# n,m = map(int,input().split())
# cnt=1
# graph = []

# for i in range(n): #그래프 그리기 
#     graph.append(list(input().rstrip()))


# dfs(0,0,cnt) #시작 0,0
# print(cnt)




# import sys
# input = sys.stdin.readline
# from collections import deque #BFS

# # 나이트 8가지 케이스 
# dx = [1,2,1,2,-1,-1,-2,-2]
# dy = [2,1,-2,-1,2,-2,1,-1]

# def bfs():
#   while queue:
#       a,b = queue.popleft() #i.j삽입 
#       for i in range(8):
#           cx = a+dx[i]
#           cy = b+dy[i]
#           if 0<=cx<n  and 0<=cy<n and graph[cx][cy]==0: #아직한번도 안간곳
#               graph[cx][cy] = graph[a][b] + 1 #칸수 더해나감 
#               queue.append([cx,cy])

# test = int(input())
# for _ in range(test):

#     # 덱선언
#     queue = deque()

#     n = int(input())
#     graph = [[0] * n for _ in range(n)] #그래프 생성

#     knight_x, knight_y = map(int,input().split()) #나이트 x,y값 
#     dochak_x, dochak_y = map(int,input().split())

#     queue.append([knight_x,knight_y])
#     bfs()
#     graph[knight_x][knight_y]=0
#     print(graph[dochak_x][dochak_y])

# import sys
# input=sys.stdin.readline

# visited = [0 for _ in range(9)]
# arr =[0]*9
# arr2=[] #찐 난쟁이


# def dfs(cnt,idx):
#     if cnt== 7: #길이가 7
#         total=0
#         for i in range(7):
#             total+=arr2[i]
#         if total==100:
#             for i in range(7):
#                 print(arr2[i])
#         return 

#     for i in range(idx,9):
#         if visited[i]==0:
#             arr2.append(arr[i])
#             visited[i]=1 #방문 
#             dfs(cnt+1,i+1)
#             visited[i]=0
#             print(arr2)
#             del arr2[-1] #마지막부분지우기 

# for i in range(9):
#     arr[i]=int(input())
# arr.sort()
# dfs(0,0)

# import sys
# input=sys.stdin.readline
# #방향벡터 
# dx = [1,-1,0,0] 
# dy = [0,0,-1,1]

# def dfs(x,y,total):
#     global cnt 
#     cnt = max(total,cnt)
#     # print(visited)
#     for i in range(4):
#         cx = x+dx[i]
#         cy = y+dy[i]
#         if 0<=cx<n  and 0<=cy<m and visited[graph[cx][cy]]!=1: #방문하지 않은 알파벳 
#             visited[graph[cx][cy]]=1
#             dfs(cx,cy,total+1)
#             visited[graph[cx][cy]]=0 
    
# n,m = map(int,input().split())

# graph = [list(map(lambda x: ord(x)-65,input().rstrip())) for _ in range(n)] #아스키 코드값으로 변환 
# #변환후 65빼줘서 0부터 A시작 
# #ord=>문자열 아스키 코드값 변환 
# visited = [0]*26
# cnt=0
# visited[graph[0][0]] = 1
# dfs(0,0,1) #시작 0,0
# print(cnt)

#2529 : 부등호 
# import sys
# from itertools import permutations

# input = sys.stdin.readline
# number = [0,1,2,3,4,5,6,7,8,9]

# k = int(input())
# arr2=[]
# allNumber=[]

# arr = input().split()
# per = permutations(number,k+1)

# for i in range(k):
#     if arr[i] == '>':
#         arr[i]=1
#     elif arr[i] == '<':
#         arr[i]=0


# # > > = 1 < = 0 이다. 
# print(list(per))
# for i in per:
#     print(i)
#     for j in range(k-1):
#         if(i[j]>i[j+1]):
#             arr2[j]=1
#         elif(i[j]<i[j+1]):
#             arr2[j]=0
#     if arr == arr2 :
#         allNumber.append[i]


# print(max(allNumber))
# print(min(allNumber))

#2529 : 부등호 
# import sys
# input = sys.stdin.readline

# k = int(input())
# arr = input().split()
# visited = [0]*10 #방문여부 
# MAX,MIN = "",""

# def check(i,j,k):
#     if k==">":
#         return i>j #맞으면 1 아니면 0 
#     else :
#         return i<j

# def bt(cnt,string):
#     global MAX,MIN
#     if cnt>k :
#         if len(MIN) == 0 :
#             MIN = string
#         else :
#             MAX = string 
#         return

#     for i in range(10):
#         if visited[i]==0:
#             if cnt == 0 or check(string[-1],str(i),arr[cnt-1]):
#                 visited[i]=1
#                 bt(cnt+1,string+str(i)) 
#                 visited[i]=0 #백트레킹 

# bt(0,"") #빈문자열에서 시작 
# print(MAX)
# print(MIN)

# import sys 
# input = sys.stdin.readline

# k=int(input())
# arr = input().split()
# visited = [0]*10
# MAX,MIN = "",""

# def check(i,j,k):
#     if k==">":
#         return i>j
#     else :
#         return i<j

# def bt(cnt,string):
#     global MAX,MIN
#     if cnt > k :
#         if len(MIN)==0: #제일 처음 들어오는거 
#             MIN = string
#         else : 
#             MAX = string #이후 MAX에 넣음 
#         return #함수반환 
#     for i in range(10):
#         if visited[i]==0: #아직 방문 전 
#             if cnt==0 or check(string[-1],str(i),arr[cnt-1]): #0이면 무조건 담꺼 붙여야함 ㅇㅇ check(string제일마지막꺼,추가될거,부호)
#                 visited[i]=1
#                 bt(cnt+1,string+str(i))
#                 visited[i]=0


# bt(0,"")
# print(MAX)
# print(MIN)

# 1700 : 멀티탭 스케줄링 

#알파벳..
# import sys
# input=sys.stdin.readline
# #방향벡터 
# dx = [1,-1,0,0] 
# dy = [0,0,-1,1]

# def BFS(x,y):
#     global cnt
#     queue = set([x,y,graph[x][y]])

#     while queue:
#         x,y,english = queue.pop()

#         for i in range(4):
#             cx = x+dx[i]
#             cy = y+dy[i]
#             if (0<=cx<n)and 0<=cy<m and graph[cx][cy] not in english:
#                 queue.add(cx,cy,english+graph[cx][cy])
#                 cnt=max(cnt,len(english)+1)


# n,m = map(int,input().split())
# graph = [list(input().strip()) for _ in range(n)]

# cnt =1 
# BFS(0,0)
# print(cnt)

#멀티탭 스케쥴링 
# import sys 
# input = sys.stdin.readline



# n,k = map(int,input().split())
# arr = list(map(int,input().split())) #사용순서 
# plug = [0 for _ in range(n)]
# cnt = 0 

# #k만큼 빙글빙글 
# for i in range(k):
#     flag = False 
#     for j in range(n):
#         if plug[j]==arr[i] or plug[]==0:
#             flag = True 
#             plug[j]=arr[i]
#             break #넣는다.
#     if flag:
#         continue
#     else :
#         a=0
#         for j in range(n):
#             try:
#                 if a<arr[i+1:].index(plug[j]):
#                     a=arr[i+1:].index(plug[j])
#                     b = j 
#             except:
#                 a = -1 
#                 b = j 
#                 break 
#         plug[b]=arr[i]
#         cnt+=1
# print(cnt)

# print(""" ---계산기---
# 1. 더하기
# 2. 빼기
# 3. 나누기
# 4. 곱하기
# 5. 나머지 
# 입력해주세요 """)
# choice = int(input())

# print("두 수를 입력해주세요")
# num1, num2 = map(int,input().split())
# if(choice==1):
#     print(num1+num2)
# elif(choice==2):
#     print(num1-num2)
# elif(choice==3):
#     print(num1//num2)
# elif(choice==4):
#     print(num1*num2)
# elif(choice==5):
#     print(num1%num2)    
# else : 
#     print("잘못된 값을 입력하셨습니다.")


# # dd
# # d
# import sys 
# input = sys.stdin.readline

# n,score,p = map(int,input().split())

# if(n<=0):
#     print(1);exit(0)

# arr = list(map(int,input().split()))
# arr.append(score)
# arr.sort(reverse=True) #내림차순으로 정렬 

# idx = arr.index(score)+1 #스코어 인덱스 출력 #공동 등수라고 해도 앞에거 출력하기에 괜춘 

# if idx>p:
#     print(-1)
# else :
#     if n==p and arr[-1]==score:
#         print(-1)
#     else: 
#         print(idx)
    
# if n==p and arr[-1]>=score: #마지막등수보다 낮은값이 입력됐을때
#     print(-1)
# else :
#     rank = n +1 
#     for i in range(n):
#         if arr[i]<=score:
#             rank = i+1 
#             break 
#     print(rank)



# #p만큼만 랭킹 리스트에 올라갈수있다
# #p를 벗어나면 랭커 x 이므로 -1출력 

#1946 : 신입 사원 
# import sys 
# input = sys.stdin.readline

# t = int(input()) #테스트 케이스 ㅍㅍㅍ
# #순위가 들어옴 
# for _ in range(t):
#     arr = []
#     seoru = 0 ; myunjeop =0 
#     ppl = int(input()) #지원자의 숫자 
#     all_num = 1 #서류1등 
#     for _ in range(ppl): 
#         s,m = map(int,input().split())
#         arr.append([s,m])
    
#     arr.sort() #서류기준 정렬 
#     maxS = arr[0][1] #먄접 첫빠따 등수 최대등수 설정 

#     for i in range(1,ppl):
#         if maxS>arr[i][1]:
#             all_num+=1
#             maxS=arr[i][1]

#     print(all_num)

# #멀티탭 
# # import sys 
# # input = sys.stdin.readline

# # n,k = map(int,input().split())
# # arr = list(map(int,input().split())) #사용순서 
# # plug = [0 for _ in range(n)]
# # cnt = 0 

# # #k만큼 빙글빙글 
# # for i in range(k):
# #     flag = False 
# #     for j in range(n):
# #         if plug[j]==arr[i] or plug[j]==0: #이미플러그에 있거나 플러그 비었을때
# #             flag = True 
# #             plug[j]=arr[i] #꼽는 과정 -> 플러그있을경우 넣어도 상관x 비었을경우는 넣어주는 과정 
# #             break 
# #     if flag: #꼽았을때 돌아가자~~
# #         continue
# #     else : #못꼽았음 ㅠㅠ 뭘빼지?
# #         a=0
# #         for j in range(n):
# #             try:
# #                 if a<arr[i+1:].index(plug[j]): #지금 플러그에 꽂혀있는게 뒤에 있다 
# #                     a=arr[i+1:].index(plug[j])
# #                     b = j #플러그에 꽂을 인덱스값 
# #             except:
# #                 a = -1 
# #                 b = j 
# #                 break 
# #         plug[b]=arr[i]
# #         cnt+=1
# # print(cnt)

#듣보잡 :1764 
# import sys 
# input = sys.stdin.readline


# n,m = map(int,input().split()) 
# cantHear=[input().strip() for i in range(n)]
# cantSee =[input().strip() for i in range(m)]

# #집합을 만들어주고 리스트로 형변환 
# #교집합 찾는다 
# cant =list(set(cantHear)& set(cantSee)) 
# print(len(cant))

# for cants in sorted(cant): #정렬값만 반환 
#     print(cants)

#!/usr/bin/env python
# print("hi")

#10828 : 스택 
# import sys 
# input = sys.stdin.readline 

# stack=[]

# n = int(input())
# for i in range(n):
#     choice = input().split()

#     if choice[0]=='push':
#         stack.append(choice[1])
#     elif choice[0]=='pop':
#         if len(stack)==0:
#             print(-1)
#         else :
#             print(stack.pop())
#     elif choice[0]=='size':
#         print(len(stack))
#     elif choice[0]=='empty':
#         if len(stack)==0: #ㅂㅣ어ㅆㅑ? 
#             print(1)
#         else :
#             print(0)
#     elif choice[0]=='top':
#         if len(stack)==0:
#             print(-1)
#         else :
#             print(stack[-1]) #마지막요소 출력 

# 큐 
# import sys 
# from collections import deque

# test = int(sys.stdin.readline())

# queue = deque()

# def empty():
#     if len(queue)==0:
#         return 1
#     else :
#         return 0 

# for _ in range(test):
#     wn = list(sys.stdin.readline().split())
#     if wn[0] == 'push':
#         queue.append(wn[1])
#     elif wn[0] == 'pop':
#         if(empty()):
#             print("-1")
#         else :
#             print(queue.popleft())
#     elif wn[0] == 'size':
#         print(len(queue))
#     elif wn[0] == 'empty':
#         if(empty()):
#             print("1")
#         else :
#             print("0")
#     elif wn[0] == 'front':
#         if(empty()):
#             print("-1")
#         else :
#             print(queue[0])
#     elif wn[0] == 'back':
#         if(empty()):
#             print("-1")
#         else :
#             print(queue[-1])

#에디터 
# L : 왼쪽, D : 오른쪽, B:왼쪽 문자 삭제, 문장 맨 앞이면 무시  P$
# import sys 
# input = sys.stdin.readline 

# word = list(input().rstrip())
# cursor=len(word)-1 #제일 마지막 문장 가르킴 

# n = int(input())

# for _ in range(n):
#     choice = input().split()
#     if choice[0]=='L':
#         if cursor==0:#제일앞이면 무시 ! 
#             continue  
#         else :
#             cursor-=1 #커서 한칸 앞 
#     elif choice[0]=='D':
#         if cursor==len(word)-1:
#             continue 
#         else :
#             cursor+=1
#     elif choice[0]=='B':
#         if cursor==0:
#             continue
#         else :
#             del word[cursor-1]
#     elif choice[0]=='P':
#         word.insert(cursor-1,choice[1])

# for words in word:
#     print(words,end="")

#1406 : 에디터 
# import sys 
# input = sys.stdin.readline

# stack1 = list(input().strip()) #커서기준 왼쪽 
# stack2=[] #커서기준 오른쪽 

# n = int(input())

# for i in range(n):
#     choice = input().split()
#     if choice[0]=='L' and stack1 != []: #왼쪽엔 아무것도 없지 않을때 
#         stack2.append(stack1.pop())
#     elif choice[0]=='D' and stack2 != []: #오른쪽엔 아무것도 없지 않을때 
#         stack1.append(stack2.pop())
#     elif choice[0]=='P':
#         stack1.append(choice[1])
#     elif choice[0]=='B' and stack1!= []:
#         stack1.pop()

# print("".join(stack1+list(reversed(stack2))))
# #join을 통해 list -> strings change 

#1026 : 보물 
# import sys 
# input = sys.stdin.readline

# n = int(input())
# total=0

# arr1=list(map(int,input().split()))
# arr2=list(map(int,input().split()))

# # #가장 작게
# for i in range(n):
#     total+=min(arr1)*max(arr2)
#     arr1.pop(arr1.index(min(arr1)))
#     arr2.pop(arr2.index(max(arr2)))
# print(total)
# arr1.sort()
# arr2.sort(reverse=True)

# for i in range(n):
#     total+=arr1[i]*arr2[i]

# print(total)

# def add(num1,num2):
#     return num1+num2

#9012 : 괄호 
# n = int(input())
# for _ in range(n):
#     cnt=0
#     stack = input() 
#     for stacks in stack:

#         if(cnt<0): #조건탈락 
#             break
        
#         if stacks =='(':
#             cnt+=1
#         else : #")"
#             cnt-=1 
        
#     if(cnt==0):
#         print("YES")
#     else :
#         print("NO")
    
#1874 : 스택 수열 
# n = int(input())
# stack1 = []
# result = []

# flag = True 

# cnt = 1
# for _ in range(n):
#     num = int(input())
#     while(cnt<=num): #1부터 붙여 
#         stack1.append(cnt)
#         result.append('+')
#         cnt+=1
#     if stack1[-1] == num:#스택의 끝부분이 입력받는 수라면 
#         stack1.pop() #팝팝 
#         result.append('-')
#     else :
#         flag = False 
# if(flag==False):
#     print("NO")
# else :
#     for results in result:
#         print(results)

#1158 : 요세푸스 문제 

# n,k = map(int,input().split())
# arr = [i for i in range(1,n+1)] #사람들 

# result = []
# idx=0 #인덱스 값으로 제거 

# for i in range(n):
#     idx+=k-1 #인덱스로제거
#     if idx>= len(arr):
#         idx%=len(arr) 
#     result.append(str(arr.pop(idx)))#idx번째숫자를 팝  str변형 


# print("<",", ".join(result)[:],">",sep="")
# print("<",end="")
# for reuslts in result:
#     print(reuslts,end=", ")

# print(">",end="")


# 1966 : 프린터 큐 
# 중요도를 체크한다 
# 중요도가 높은게 단 하나라도 있을 경우 맨 뒤로 보낸다

# test = int(input())

# for _ in range(test):
#     n,m = map(int,input().split()) #n : 문서 갯수 m: 몇번째?
#     arr = list(map(int,input().split())) #중요도 
#     mPlace=[0 for _ in range(n)]
#     mPlace[m]=1 #찾고싶은 위치 표시 
#     cnt =0 

#     while True :
#         if arr[0]==max(arr): #제일 첫번째 요소가 최댓값이라면 
#             cnt+=1 
#             if mPlace[0]==1: #찾던값 
#                 print(cnt)
#                 break 
#             else :
#                 del arr[0]
#                 del mPlace[0] #필요 없는 값 삭제 
#         else :
#             arr.append(arr.pop(0)) #최댓값이 아닌 경우 뒤에 붙이기 
#             mPlace.append(mPlace.pop(0)) #뒤로 붙이기 

# 5430 : AC 
# R : 뒤집기 D: 버리기 
# 비어있는데 버리면 에러 발생 
# 함수 조합해서 사용가능 


# import sys 
# input = sys.stdin.readline

# test = int(input())
# for _ in range(test):
#     func = input() 
#     n = int(input())
#     queue = input().strip()[1:-1].split(',')
#     func = func.replace('RR',"")
#     r=0
#     first,back=0,0

#     for funcs in func:
#         if funcs == 'R':
#             r+=1
#         elif funcs=='D':
#             if r%2 == 0 :
#                 first+=1 #앞부분 컷
#             else :
#                 back+=1 #뒷부분 컷

#조건여부에 따라 출력 
    # if first+back<=n:
    #     queue=queue[first:n-back]

    #     if r%2 == 1:
    #         print("["+','.join(queue[::-1])+']')
    #     else :
    #         print("["+','.join(queue)+']')
    # else :
    #     print("error")

# score1 = int(input("국어 점수를 입력하세요."))
# print("수학 점수를 입력하세요. ",end="")
# score2 = int(input())
# print("영어 점수를 입력하세요. ",end="")
# score3 = int(input())

# total=score1+score2+score3
# average =  (total)/3

# print("총점 : ", (total))
# print("평균 : " ,round(average, 2))
# print(f"평균 : {round(average,2)}")
#6603 :로또
# from itertools import combinations

# while True:
#     lotto = list(input().split())

#     if (lotto[0]=='0'): #종료  
#         break 
#     del lotto[0]
#     lottos = list(map(' '.join,combinations(lotto,6)))
#     for lottoss in lottos:
#         print(lottoss)
#     print()


#1182 : 부분수열의 합 
# import sys 
# from itertools import combinations

# input = sys.stdin.readline

# n,s = map(int,input().split())
# # 더한값이 s가 되게 만들기 
# # 부분수열 갯수 구하기 
# arr = list(map(int,input().split()))
# cnt=0

# for i in range(1,n+1):
#     arr2 = combinations(arr,i) #i만큼 조합 생성
    
#     for j in arr2:
#         if sum(j)==s:
#             cnt+=1 

# print(cnt)

#재귀 풀이 익히기 
# import sys
# input = sys.stdin.readline
# def dfs(idx, sum):
#     global cnt
#     if idx >= n:
#         return
#     sum += s_[idx]
#     if sum == s:
#         cnt += 1
#     dfs(idx + 1, sum - s_[idx])
#     dfs(idx + 1, sum)
# n, s = map(int, input().split())
# s_ = list(map(int, input().split()))
# cnt = 0
# dfs(0, 0)
# print(cnt)

# 9095 : 1,2,3 더하기


규칙 
f(n)=f(n-1)+f(n-2)+f(n-3)
def OneTwoThree(n):
    if n==1:
        return 1
    elif n==2:
        return 2
    elif n==3:
        return 4
    else :
        return OneTwoThree(n-1)+OneTwoThree(n-2)+OneTwoThree(n-3)
case=[1,2,4]
t = int(input())

for i in range(3,10):
    case.append(case[i-3]+case[i-2]+case[i-1])

for _ in range(t):
    n = int(input())
    print(case[n-1])
