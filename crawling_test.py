import requests
from bs4 import BeautifulSoup

def sangrok1():
    url = "http://dgucoop.dongguk.edu/mobile/menu.html?code=7"
    res = requests.get(url)
    res.encoding = None
    html = res.text

    bs = BeautifulSoup(html, "html.parser")

    tags_td = bs.findAll("td")
        
    if tags_td[3].text == None :
        menu = "🥲 현재 상록원 1층 생활협동조합에 등록된 메뉴가 없습니다."
    else :
        # menu_text
        # 0번째 : 시간
        # 1,3,5..홀수번째 : 이름 
        # 2,4,6,8.. 짝수번째 : 원산지+가격  => 공백 기준으로 스플릿하면 또 나눌 수 있을듯
        menu_text = tags_td[3].text.split('\r\n')
        
        menu = f"🍳 상록원 1층\n\n⏰ 운영시간 : {menu_text[0]}\n\n--------🍴 중석식 🍴---------\n"
        # 어차피 메뉴 1에 모두 등록 해뒀으니, 제일 위에거만 읽어오면 됨
        
        for i in range(1, len(menu_text)) :
            text = menu_text[i]
            
            # 원산지가 있을때 
            if text[0] == '(':
                locationPrice = text.split()
                # 원산지만 적혀 있는 경우 
                if len(locationPrice) == 1:
                    continue
                # 원산지, 가격 모두 있는 경우 
                # 텍스트는 가격으로 설정 
                text = locationPrice[1]
            
            # 메뉴와 가격이 한줄에 적혀있을 경우
            if len(list(text.split())) == 2:
                menu = menu + list(text.split())[0] + "\n" + list(text.split())[1] + "\n"
            else :
                menu = menu + text + " " +"\n" 
            # if len(text) == 0:
            #     continue
            
    return  menu

print(sangrok1())