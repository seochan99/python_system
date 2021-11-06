def solution(s):
    s2 = s[::-1]
    num=1
    answer = []
    if(s[-1]==s[0]): #처음과 끝이 같은 경우 
        num+=1
        for i in range(len(s2)-1):#마지막문자열잇기 
            if s2[i]==s2[i+1]:
                num+=1
            else :
                break 
        for i in range(len(s)-1):
            if s[i]==s[i+1]:
                num+=1
            else:
                answer.append(num)
                num=1
    else :#처음끝 다름 
        print("hi")
        for i in range(len(s)-1):
            if s[i]==s[i+1]:
                num+=1
            else:
                answer.append(num)
                num=1
    # answer.sort()
    return answer


s="wowwow"
print(solution(s))