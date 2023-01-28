
# Matrix 열과 행을 계산하여 90도 회전 시켜주는 함수 
def rotate_90(a):
    n = len(a)
    m = len(a[0])
    result = [[0]*n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = a[i][j] 
    return result 

#모두 1인지 확인 함수 
def check(matrix): 
    lock_length = len(matrix) // 3
    for i in range(lock_length,lock_length * 2):
        for j in range(lock_length,lock_length*2):
            if matrix[i][j] != 1:
                return False 
    return True 