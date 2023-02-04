import smtplib
from email.mime.text import MIMEText

def requestMail():
    # 세션 생성
    s = smtplib.SMTP('smtp.gmail.com', 587)
    # TLS 보안 시작
    s.starttls()
    # 로그인 인증
    s.login('onepoint357@gmail.com', 'xkordlwkyxfeiwor')
    msg = MIMEText(f"캠퍼스 투어 신청이 왔습니다.")
    msg['Subject'] = '[동감] 캠퍼스투어 신청'
    s.sendmail("onepoint357@gmail.com", "onepoint357@gmail.com", msg.as_string())
    # 세션 종료
    s.quit()

requestMail()