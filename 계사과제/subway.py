import csv
import matplotlib.pyplot as plt

# 변수 f에 subwayfee.csv파일을 저장한다.
f = open('/Users/seochan/Documents/GitHub/python_system/계사과제/subwayfee.csv')
data = csv.reader(f)  # 파일을 열어서 data에 list형태로 한 행씩 넣는다.

next(data)  # 헤더 패스

maxNumber = [0]*4  # 0으로 4칸 초기화
maxNumber_station = [""]*4  # 빈문자열로 4칸 초기화
label = ["유임승차", "유임하차", "무임승차", "무임하차"]

rate = 0

for row in data:
    for i in range(4, 8):  # 4~7
        row[i] = int(row[i])
        if row[i] > maxNumber[i-4]:
            maxNumber[i-4] = row[i]  # 최대수 저장
            maxNumber_station[i-4] = row[3] + ' '+row[1]  # 최대 수의 역과 호선 저장

for i in range(4):
    print(f"{label[i]} : {maxNumber_station[i]} {maxNumber[i]}")
