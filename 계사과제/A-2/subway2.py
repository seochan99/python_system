
import csv
from matplotlib import rc
import matplotlib.pyplot as plt

f = open('/Users/seochan/Documents/GitHub/python_system/계사과제/A-2/subwayTime.csv')
data = csv.reader(f)
next(data)
next(data)

s_in = [0] * 24     # 승차 인원 저장 리스트 초기화
s_out = [0] * 24    # 하차 인원 저장 리스트 초기화

for row in data:
    row[4:] = map(int, row[4:])
    for i in range(24):
        s_in[i] += row[4+i*2]
        s_out[i] += row[5+i*2]

rc('font', family='AppleGothic')  # 이 두 줄을
plt.rcParams['axes.unicode_minus'] = False

plt.title('지하철 시간대별 승하차 인원 추이')  # 제목 추가
plt.plot(s_in, label='승차')             # 승차 인원을 꺾은선 그래프로 표현
plt.plot(s_out, label='하차')            # 하차 인원을 꺾은선 그래프로 표현
plt.legend()
plt.xticks(range(24), range(4, 28))
plt.show()
