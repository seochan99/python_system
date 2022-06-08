import random

staffFirst = ["김치만", "은하수", "남산골", "산타돈부리", "닭칼국수", "홍짜장"]
staffFirstTeam = [1, 2, 3, 4, 5, 6]

random.shuffle(staffFirst)

for i in range(1):
    print(f"갈 곳 : {staffFirst[i]}")
