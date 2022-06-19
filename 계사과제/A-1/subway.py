import csv
import matplotlib.pyplot as plt  # 파이차트를 위한 모듈 추가
from matplotlib import rc


# 변수 f에 subwayfee.csv파일을 저장한다.
f = open('/Users/seochan/Documents/GitHub/python_system/계사과제/A-1/subwayfee.csv')
data = csv.reader(f)  # 파일을 열어서 data에 list형태로 한 행씩 넣는다.

next(data)  # 헤더 패스

maxNumber = [0]*4  # 0으로 4칸 초기화
maxNumber_station = [""]*4  # 빈문자열로 4칸 초기화
label = ["유임승차", "유임하차", "무임승차", "무임하차"]

c = ["#14CCC0", "#389993", "#FF1C6A", "#CC14AF"]  # 색상

rc('font', family='AppleGothic')  # 이 두 줄을
plt.rcParams['axes.unicode_minus'] = False


rate = 0

for row in data:
    for i in range(4, 8):  # 4~7
        row[i] = int(row[i])
    plt.figure(dpi=300)
    plt.title(row[3]+' '+row[1])  # 제목
    plt.pie(row[4:8], labels=label, colors=c, autopct='%1.f%%')
    plt.axis('equal')
    plt.savefig(row[3]+' '+row[1]+'png')
    plt.show()
