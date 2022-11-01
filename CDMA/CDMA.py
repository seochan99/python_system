import numpy as np

# 4개의 전송 프로세스(t0, t1, t2, t3)
t0 = [1, 1, 1, 1, 1, 1, -1, -1]
t1 = [1, -1, 1, -1, -1, -1, 1, 1]
t2 = [1, 1, -1, -1, 1, 1, 1, 1]
t3 = [1, -1, -1, 1, 1, -1, -1, 1]

# biplor chip List
bipolar = []

# 4개의 바이폴라 형태로 된 칩 시퀀스 입력받기
print("4개의 바이폴라 비트를 입력하시오.(예시 : 1 0 1 0)")
bipolar = list(map(int, input().split()))

# 4개의 수신 프로세스(r0, r1, r2, r3)
# 각 전송 프로세스가 1Bit씩 할당받음
r0 = np.multiply(t0, bipolar[0])
r1 = np.multiply(t1, bipolar[1])
r2 = np.multiply(t2, bipolar[2])
r3 = np.multiply(t3, bipolar[3])

print()

# joiner 프로세스, 신호 결합
joinerProcess = r0+r1+r2+r3
print("joinerProcess :", joinerProcess)

print()

# 수신 신호에서 수신된 비트 계산
inner_product_r0 = np.multiply(joinerProcess, t0)
inner_product_r1 = np.multiply(joinerProcess, t1)
inner_product_r2 = np.multiply(joinerProcess, t2)
inner_product_r3 = np.multiply(joinerProcess, t3)


# 수신 프로세스가 출력하는 표준출력
print(f"standard output r0 : {inner_product_r0}")
print(f"standard output r1 : {inner_product_r1}")
print(f"standard output r2 : {inner_product_r2}")
print(f"standard output r3 : {inner_product_r3}")
