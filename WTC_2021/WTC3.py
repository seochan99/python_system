def solution(ings, menu, sell):
    ingsArr=[]
    menuArr=[]
    sellArr=[]
    for ingss in ings:
        ingsArr.append(ingss.split(" "))
    for menus in menu:
        menuArr.append(menus.split(" "))
    for sells in sell:
        sellArr.append(sells.split(" "))

    #재료비 구하기 
    for i in range(len(menuArr)):
        priceMenu=0
        for j in range(len(ingsArr)):
            if ingsArr[j][0] in menuArr[i][1]:
                priceMenu+=int(ingsArr[j][1])*(menuArr[i][1].count(ingsArr[j][0]))
        menuArr[i][2]=int(menuArr[i][2])-int(priceMenu) #가격->순이익 
    total=0

    for i in range(len(sellArr)):
        for j in range(len(menuArr)):
            if(sellArr[i][0]==menuArr[j][0]):
                total+=menuArr[j][2]*int(sellArr[i][1])
    return total #총 수익 

ings = ["r 10", "a 23", "t 124", "k 9"]
menu = ["PIZZA arraak 145", "HAMBURGER tkar 180", "BREAD kkk 30", "ICECREAM rar 50", "SHAVEDICE rar 45", "JUICE rra 55", "WATER a 20"]
sell = ["BREAD 5", "ICECREAM 100", "PIZZA 7", "JUICE 10", "WATER 1"]
print(solution(ings,menu,sell))