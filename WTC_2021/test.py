#########1############################
# def main(): 
#     arr = list(map(int,input().split()))

#     for i in range(1,arr[0]+1):
#         check=0
#         max = arr[i]
#         for j in range(i+1,arr[0]+1):
#             if(arr[j]>max):
#                 print(j,end=" ")
#                 check=1
#                 break
#         if check==0:
#             print(-1,end=" ")

# if __name__=="__main__": 
#     main()


#########3##################

#균형 3진법이란 ? 
#(-1,0,1) 를 3^n과 곱해서 나타내는 법 
def ternary(n):#균형 3진법 함수 
   result = ""
   sam=["0","1","-1"]
   while n:
       result = result + sam[n % 3] + " "
       n = (n+1)//3
   return result 
# 2-> -1 1
def main(): 
    n = int(input())
    print(ternary(n))   #n을 ternary 함수에 대입후 결과 값 출력하기 


if __name__=="__main__": 
    while(True):
        main()
        print("---------------")
    
############4##########
# def main(): 
#     arr = list(input().split(';'))
#     print(arr)
#     for i in range(3):
#         arr[i]=int(arr[i])

#     subject = [];seosul=[];mokjeok=[]
#     if arr[0]==0 or arr[1]==0 or arr[2]==0:
#         print("No Possible sentence.;")

#     for i in range(3,3+arr[0]):
#         subject.append(arr[i])

#     for i in range(3+arr[0],3+arr[0]+arr[1]):
#         seosul.append(arr[i])

#     for i in range(3+arr[0]+arr[1],3+arr[0]+arr[1]+arr[2]):
#         mokjeok.append(arr[i])
        
#     for i in range(arr[0]):
#         for j in range(arr[1]):
#             for k in range(arr[2]):
#                 print(f"{subject[i]} {seosul[j]} {mokjeok[k]};",end="")
#     print("")

# if __name__=="__main__": 
#     main()