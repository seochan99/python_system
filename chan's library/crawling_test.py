import re
import requests
from bs4 import BeautifulSoup
from datetime import datetime
now = datetime.now()

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
        
        menu = f"\n\n🍳 상록원 1층\n\n⏰ 운영시간 : {menu_text[0]}\n\n------🍴 중석식 🍴-------\n\n"
        # 어차피 메뉴 1에 모두 등록 해뒀으니, 제일 위에거만 읽어오면 됨
        
        # 가격, 음식이름 구분
        flag = False

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
                menu = menu + "🏷️ " +list(text.split())[0] +" - "+list(text.split())[1] + "\n"
            else :
                if(flag==False):
                    menu = menu +"🏷️ "+ text.replace('*','&') + " - " 
                    flag=True
                else :
                    menu = menu + text + " " +"\n"
                    flag = False
    return  menu

# 상록원 2층
def sangrok2():
    url = "http://dgucoop.dongguk.edu/mobile/menu.html?code=1"          # 상록원 2층 페이지
    res = requests.get(url)                                             # 페이지 데이터 가져오기 
    res.encoding = None
    html = res.text                                                     # 페이지 HTML 정보 저장

    bs = BeautifulSoup(html, "html.parser")                             # HTML 파싱

    tags_td = bs.findAll("td")                                          # td 태그 추출
    if tags_td[4].text == "" :                                        # 조식 백반에 메뉴 없을 경우 상록원 2층 메뉴 없음
        menu = "🥲 현재 상록원 2층 생활협동조합에 등록된 메뉴가 없습니다."
    else :
        menu = "======= 상록원2층 =======\n"+"———"+tags_td[1].text+"———\n"# '----중식----'
        for i in [0,1] :
            idx = 3
            for j in range(7+i, len(tags_td), 3) :
                idx = idx + 3
                if(i == 1 and j == 8) :
                    menu = menu+"\n———"+tags_td[2].text+"———\n"         # '----석식----'
                if(len(tags_td[j]) == 0) :                              # 메뉴 없을 경우 건너뛰기
                    continue
                menu = menu+"<"+tags_td[idx].text+">\n"                 # '<일품>', '<양식>', '<뚝배기>'

                text = re.sub("<span.*</span>", "",str(tags_td[j]))     # 중식 일품, 중식 양식, 중식 뚝배기, ..., 석식 뚝배기 순서대로 메뉴 저장
                text = re.sub("<.*?>","",text).replace("amp;","")

                if(text.find("￦") >= 0) :                              # ￦가 있는 경우
                    text = text.replace("￦ ", " ￦")                   # '￦ ' -> ' ￦'
                else :                                                  # ￦가 없는 경우
                    text = text.replace(" ", " ￦").replace("원", "")   # ' ', ' 원' -> ' ￦'
                menu = menu+text+"\n"

        #백반 추가                                                      # 이때랑 지금이랑 상록원 2층 페이지 형식이 달라진 건감..? 뭔가 안 맞아..!
        menu = menu+"\n——— 중식&석식 ———\n<"+tags_td[3].text+">\n"      #
        #백반 메뉴 추가                                                 #
        text = re.sub("T\S*\r\n.*\r\n", "",tags_td[4].text)            #
        menu = menu+text+"\n"
    return menu

def sangrok3():
    url = "http://dgucoop.dongguk.edu/mobile/menu.html?code=5"          # 상록원 3층 페이지
    res = requests.get(url)                                             # 페이지 데이터 가져오기 
    res.encoding = None
    html = res.text                                                     # 페이지 HTML 정보 저장

    bs = BeautifulSoup(html, "html.parser")                             # HTML 파싱

    tags_td = bs.findAll("td")                                          # td 태그 추출

    #tags_td[1].text : 중식
    menu = f"\n\n🍳 상록원 3층\n\n⏰ 운영시간 : 11:00 ~ 14:00\n\n------🍴 중식 🍴-------\n\n"

    for i in [0,1] :
        for j in range(4+i, len(tags_td)-2, 3) :
            if(i == 1 and j == 5) :
                menu = menu+"\n———"+tags_td[2].text+"———\n"             # '----석식----'
            text = tags_td[j].text                                      # 중식 메뉴1, 중식 메뉴2, 석식 메뉴1, 석식 메뉴2 순서대로 저장
            if(len(text) == 0) :                                        # 메뉴 없을 경우 건너뛰기
                continue

            text = text.replace("￦ ", " ￦")                           # '￦ ' -> ' ￦'
            text = re.sub("<span.*</span>", "",str(tags_td[j]))
            text = re.sub("\(\S*\)\r\n", "", text)
            text = re.sub("<.*?>","",text)

            menu = menu+text+"\n"

    # 채식당
    veget = re.sub("<span.*</span>", "",str(tags_td[10]))          
    veget = veget.replace("*외부고객 -10000원<br/><br/>", "").replace("-", " ￦").replace("원￦ ", "\n￦")
    veget = re.sub("<.*?>","",veget)

    menu = menu+"\n———"+tags_td[9].text+"———\n"+veget                   # 채식당 메뉴 저장
    return menu
print(now.hour)
print(sangrok3())