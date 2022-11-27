# 사다리 알고리즘
import random
import time

firstPresentation = ["1팀", "2팀", "3팀", "4팀", "5팀", "6팀", "7팀",
                     "8팀", "9팀", "10팀", "11팀", "12팀", "13팀"]
firstPresentationTeam = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


random.shuffle(firstPresentation)
for i in range(4):

    print(f"{firstPresentationTeam[i]}번째 순서 : {firstPresentation[i]}")
    time.sleep(2)
