def solution(log):
    arr=[]
    total=0
    for logs in log:
        arr.append(logs.split(":"))

    for i in range(len(log)//2):
        hours = int(arr[2*i+1][0])-int(arr[2*i][0]) #hour 
        mins =int(arr[2*i+1][1]) - int(arr[2*i][1]) #min 

        #hour -> min 변환 
        hours=hours*60
        mins = hours+mins

        #min예외처리 
        if(mins<5):
            continue
        if(mins>=105):
            mins=105
        total+=mins
    
    #total -> 시간으로 
    resultHour = total//60 
    resultMin = total%60 
    if(resultHour<10):
        resultHour="0"+str(resultHour)
    if(resultMin<10):
        resultMin="0"+str(resultMin)

    answer = str(resultHour)+":"+str(resultMin)
    return answer


log = ["08:30", "09:00", "14:00", "16:00", "16:01", "16:06", "16:07", "16:11"]
print(solution(log))