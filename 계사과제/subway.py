import csv
# 변수 f에 subwayfee.csv파일을 저장한다.
f = open('/Users/seochan/Documents/GitHub/python_system/계사과제/subwayfee.csv')
data = csv.reader(f)  # 파일을 열어서 data에 list형태로 한 행씩 넣는다.

for row in data:
    print(row)  # 출력한다.
