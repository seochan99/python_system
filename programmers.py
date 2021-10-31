## 프로그래머스 level 1 : x만큼 간격 

# #내풀이 
# def solution(x,n):
#     answer = []
#     for i in range(n):
#         answer.append(x*(i+1))
#     return answer

# #다른사람풀이 
# def solution(x,n):
#     return [i*x+x for i in range(n)]

# 핸드폰 번호 가리기

# def solution(phone_number):
#     return "*"*(len(phone_number)-4) + phone_number[-4:]

# print(solution("01023624076"))

#행렬의 덧셈 
# def solution(arr1, arr2):
#     answer = [[]]
#     answer.append(arr1[0]+arr2[0])
#     return answer
