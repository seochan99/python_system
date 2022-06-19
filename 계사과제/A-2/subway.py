import csv
import matplotlib.pyplot as plt
from matplotlib import rc


f = open('/Users/seochan/Documents/GitHub/python_system/계사과제/A-2/subwayTime.csv')
data = csv.reader(f)

next(data)
next(data)

maxNum = [0]*24  # 시간대별 최대 승차 인원 저장 리스트
maxNumStation = [""]*24  # 시간대버ㅕㄹ 최대 승차 인원 역 이름


for row in data:
    row[4:] = map(int, row[4:])
    for j in range(24):
        # a = row[j*2+4]
        b = row[5+j*2]
        if b > maxNum[j]:
            maxNum[j] = b
            maxNumStation[j] = row[3]

maxNumStation[j] = row[3]+'('+str(j+4)+')'  # x축에 몇시인지 알려주기

rc('font', family='AppleGothic')  # 이 두 줄을
plt.rcParams['axes.unicode_minus'] = False

plt.bar(range(24), maxNum)
plt.xticks(range(24), maxNumStation, rotation=90)
plt.show()
