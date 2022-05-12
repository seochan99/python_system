# 사다리 알고리즘

import random

# 선발대 운영진
staffFirst = ["김태연", "백지원", "서희찬", "이슬기", "정민경", "이건회", "신예진", "안석환"]
staffFirstTeam = [1, 1, 2, 2, 3, 3, 4, 4]

# 후발대 운영진
staffLast = ["강동희", "김수영", "정준홍", "안소은", "박상준"]
staffLastTeam = [1, 2, 3, 4, 4]

# 선발대 학생
studentFirst = ["김성준", "박영신", "오민영", "오준서", "유다현", "윤영서",
                "이영서", "한수연", "한주아", "홍세림", "이예나", "안유성", "이유진"]
studentFristTeam = [1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4]

# 후발대 학생
studentLast = ["김나연", "김재니", "이상돈", "서연미", "장여신", "이지영"]
studentLastTeam = [1, 1, 2, 2, 3, 4]

random.shuffle(staffFirst)
random.shuffle(staffLast)
random.shuffle(studentFirst)
random.shuffle(studentLast)

print("-------운영진 선발대-------")

for i in range(8):
    print(f"{staffFirstTeam[i]}팀 : {staffFirst[i]}")

print("-------운영진 후발대-------")

for i in range(5):
    print(f"{staffLastTeam[i]}팀 : {staffLast[i]}")

print("-------10기 선발대-------")

for i in range(13):
    print(f"{studentFristTeam[i]}팀 : {studentFirst[i]}")

print("-------10기 후발대-------")

for i in range(6):
    print(f"{studentLastTeam[i]}팀 : {studentLast[i]}")
