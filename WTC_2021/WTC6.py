def solution(time, plans):
    time = int(time*60) #시간 ->분으로 만들기 
    restTime=0
    allTime=[]
    for i in range(len(plans)):
        #24시간제로 변경 
        if  "AM" in plans[i][1]:
            plans[i][1] = int(plans[i][1][0:-2])
        elif "PM" in plans[i][1]:
            plans[i][1] = int(plans[i][1][0:-2])+12

        if  "AM" in plans[i][2]:
            plans[i][2] = int(plans[i][2][0:-2])
        elif "PM" in plans[i][2]:
            plans[i][2] = int(plans[i][2][0:-2])+12

        if(plans[i][1]<18): #퇴근시간보다 빨리 출발 
            if(plans[i][1]<9.5): #출근시간보다 빨리 출발 
                restTime+=8.5
            else : #출근시간보다 늦고 출발  퇴근보다 빨리 
                restTime+=(18-plans[i][1])

        #도착할때 
        if(plans[i][2]>13): #도착시간보다 늦게 도착 
            if(plans[i][2]>18): #퇴근시간보다 늦게 도착
                restTime+=5
            else : #퇴근시간보다 빠르고 출근시간보다 늦게 도착 
                restTime+=(plans[i][2]-13)
        allTime.append(restTime*60) #붙이기 
    for i in range(len(allTime)):
        if allTime[i]<=time: #휴가시간보다 이하라면 여행 가능 
            answer = ""+plans[i][0]
    return answer

time = 3.5
plans = [ ["홍콩", "11PM", "9AM"], ["엘에이", "3PM", "2PM"] ]
#금요일 9시30분 출근 18시 퇴근
#토요일 13시 출근 18시 퇴근 

#time = 남은 휴가 시간 
#plans =여행 가능한곳, 금요일 출발시간, 월요일 도착시간 
print(solution(time,plans))