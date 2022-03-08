import pandas

#다운받은 구글 스프레드시트 파일 경로를 넣어주세요
df = pandas.read_csv("/Users/seochan/Documents/Github/python_system/10기모집/sheet.csv")
questions = df.columns.tolist()

for i in range(3,len(df)):
    # 지원자명.md로 생성됩니다.
    # 동명이인이 있는 경우 학번 등을 추가로 붙여주시면 될거같습니다.
    # questions[3] : 지원자 성함
    f = open("/Users/seochan/Documents/Github/python_system/10기모집/사람/" + df.loc[i,questions[3]] + ".md","w")
    for q in questions:
        f.write("## " + q + "\n")
        f.write(str(df.loc[i,q]))
        f.write("<br><br>\n\n\n")
    f.close()