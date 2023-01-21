# 파일 오픈
f = open("/Users/seochan/Documents/GitHub/python_system/systemsofrware/optab.txt", 'r')

# 지시문, 코드 리스트
instruction = []
code = []

# 파일 정보 저장
while True:
    line = f.readline()
    if not line:                                # 파일 읽기 스탑
        break
    # 개행 없애고 공백기준 split하여 List화 하여 temp에 임시 저장
    temp = line.rstrip('\n').split()
    # temp[0] : instruction, temp[1] : code이므로 각각의 list에 저장
    instruction.append(temp[0])
    code.append(temp[1])

# 파일 닫기
f.close()

# 안내문
print("---instruction : code---")
# 현재 instrcutuon, code 리스트내용을 대응 시켜서 보여줌
for i in range(len(instruction)):
    print(f"{instruction[i]} : {code[i]}")


# intruction 실행
while True:
    flag = False                        # 지시문 있는지 체크하기 위한 flag
    ins = input("\ninstrctuon(EXIT : Q) : ")                # 지시문 받기

    # Q입력시 프로그램 종료
    if ins == 'Q':
        print("END PROGRAM")
        break
    # 지시문 만큼 반복
    for i in range(len(instruction)):
        # 지시문리스트의 요소와 입력한 값이 동일할때
        if instruction[i] == ins:
            # 해당 지시문의 code출력
            print(f"code : {code[i]}")
            # 깃발 True로
            flag = True
            # 현재 반복문 종료
            break
    # 지시문없으면 아래 문구 출력
    if flag == False:
        print("해당 지시문에 맞는 code가 없습니다.")  # 해당 지시문 없으면뜨는 에러
