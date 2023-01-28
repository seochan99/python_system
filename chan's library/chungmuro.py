import random

Foodcours = ["모리짱", "KFC", "버거킹+생맥", "썬더치킨+생맥", "김치만"]
random.shuffle(Foodcours)

for i in range(1):
    print(f"갈 곳 : {Foodcours[i]}")
