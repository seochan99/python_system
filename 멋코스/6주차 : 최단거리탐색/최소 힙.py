import heapq 

#오름차순 힙 정렬 
def heapsort(iterable):
    h = []
    result = []
    #모든 원소를 차례대로 힙에 삽입 
    for value in iterable:
        heapq.heappush(h,value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(heapq.heappop(h))
        #우선순위가 높은거부터 뽑아낸다.
    return result 

result = heapsort([1,3,5,7,9,2,4,6,8,0])
print(result)