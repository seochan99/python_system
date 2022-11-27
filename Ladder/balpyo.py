# 사다리 알고리즘
import random
import time

mid = ["권은빈", "구가영", "서희찬", "정승연"]
midTeam = [1, 2, 3, 4]


random.shuffle(mid)
for i in range(4):

    print(f"{midTeam[i]}번째 순서 : {mid[i]}")
    time.sleep(2)
