# 사다리 알고리즘
import random
import time
from datetime import datetime


# 기획/디자인 : 4명
planDesign = ["박현웅", "서연미", "장여신", "이영서"]
planDesignTeam = [1, 2, 3, 4]

# 백엔드 : 11명
backend = ["김재니", "류슬기", "박영신", "박영웅",
           "안유성", "오민영", "윤영서", "이유진", "이지영", "한수연", "한주아"]
backendTeam = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4]

# 프론트엔드 : 5명
frontend = ["김윤성", "오준서", "유다현", "이상돈", "이예나"]
frontendTeam = [1, 2, 3, 4, 4]

# 리스트 섞기
random.shuffle(planDesign)
random.shuffle(backend)
random.shuffle(frontend)

# 4팀
team1 = []
team2 = []
team3 = []
team4 = []

time.sleep(3)
print("\n-------기획/디자인-------")
for i in range(4):
    print(f"{planDesignTeam[i]}팀(기획/디자인): {planDesign[i]}")

    # 기획/디자인 팀에 넣기
    if planDesignTeam[i] == 1:
        team1.append(planDesign[i])
    elif planDesignTeam[i] == 2:
        team2.append(planDesign[i])
    elif planDesignTeam[i] == 3:
        team3.append(planDesign[i])
    elif planDesignTeam[i] == 4:
        team4.append(planDesign[i])
print("-------------------------\n")

time.sleep(3)
print("\n-------백엔드-------")
for i in range(11):
    print(f"{backendTeam[i]}팀(백엔드) : {backend[i]}")

    # 백엔드 팀에 넣기
    if backendTeam[i] == 1:
        team1.append(backend[i])
    elif backendTeam[i] == 2:
        team2.append(backend[i])
    elif backendTeam[i] == 3:
        team3.append(backend[i])
    elif backendTeam[i] == 4:
        team4.append(backend[i])
print("--------------------\n")

time.sleep(3)
print("\n-------프론트엔드-------")
for i in range(5):
    print(f"{frontendTeam[i]}팀(프론트엔드) : {frontend[i]}")

    # 프론트엔드 팀에 넣기
    if frontendTeam[i] == 1:
        team1.append(frontend[i])
    elif frontendTeam[i] == 2:
        team2.append(frontend[i])
    elif frontendTeam[i] == 3:
        team3.append(frontend[i])
    elif frontendTeam[i] == 4:
        team4.append(frontend[i])
print("------------------------\n")

time.sleep(4)
print(f"팀1 : {team1}")
print(f"팀2 : {team2}")
print(f"팀3 : {team3}")
print(f"팀4 : {team4}")
