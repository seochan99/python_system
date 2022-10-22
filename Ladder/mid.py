# 사다리 알고리즘
import random
import time

mid = ["1팀", "2팀", "3팀", "4팀"]
midTeam = [1, 2, 3, 4]


random.shuffle(mid)
for i in range(4):

    print(f"{midTeam[i]}번째 순서 : {mid[i]}")
    time.sleep(2)
