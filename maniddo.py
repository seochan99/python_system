import smtplib
import random

from email.mime.text import MIMEText

# 세션 생성
s = smtplib.SMTP('smtp.gmail.com', 587)

# TLS 보안 시작
s.starttls()

# 로그인 인증
s.login('gmlcks00513@gmail.com', 'rrzxtnjwyweybxqq')

# 마니또 받는 사람 
likelion = ["김수영","김윤성","류슬기","김재니","이유진","이여원","박영신","서희찬","오준서","윤영서","이영서","안유성","이상돈","한수연"]
likelion_mail = [
    'ksoo5386@dgu.ac.kr','k29445037@gmail.com','lyuseulgi05@gmail.com','kjn3008@gmail.com',
    'violelove06@gmail.com','lywon725@naver.com','2022110233@dgu.ac.kr','gmlcks0513@naver.com',
    'dhwnstj701@gmail.com','yys020819@gmail.com','youngseo28@dgu.ac.kr','ustar1210@dgu.ac.kr',
    '2019112491@dgu.ac.kr','suyeon06233@gmail.com']
# 마니또 
shuffle_likelion = ["김수영","김윤성","류슬기","김재니","이유진","이여원","박영신","서희찬","오준서","윤영서","이영서","안유성","이상돈","한수연"]


# 중복 제거 처리 
while True :
    flag = True 
    random.shuffle(shuffle_likelion)
    for i in range(14):
        # 동일요소가 있다면 다시 셔플 진행 
        if likelion[i] == shuffle_likelion[i]:
            flag = False 
            break 
    # 중복이 없다면 flag는 True 
    if flag:
        break

for i in range(14):
    msg = MIMEText(f'안녕하세요! {likelion[i]}님!! \n 당신의 마니또는 {shuffle_likelion[i]}입니다! 예산은 5,000원이며 마니또의 선물을 준비해주세요!')
    msg['Subject'] = '🦁동대멋사 운영진 엠티 마니또🦁'
    s.sendmail("gmlcks00513@gmail.com", f"{likelion_mail[i]}", msg.as_string())
# 세션 종료

s.quit()