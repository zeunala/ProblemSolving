'''
눈덩이 굴리기

입력
첫째 줄에 공백을 기준으로 앞마당의 길이 N(1<=N<=100), 대회의 시간 M(1<=M<=10)이 주어진다.
둘째 줄에 길이가 N인 수열 a가 주어진다. (1<=ai<=1000000)

출력
첫째 줄에 대회 시간 내에 가장 크게 만들 수 있는 눈덩이의 크기를 출력한다.
'''

'''
- 대회의 시간이 최대 10이고 가능한 동작은 +1칸/+2칸 2개 뿐이므로 모든 경우의 수를 체크한다.
* Pass/1st/00:10:53
'''
from itertools import product

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.insert(0, 0) # 인덱스 1부터 시작하기 위함

maxSize = 0
# ex. (1, 1, 1, 2): 1칸, 1칸, 1칸, 2칸 순으로 이동
for case in list(product([1, 2], repeat = M)):
    currentSize = 1 # 현재까지 싸인 눈의 크기
    currentIdx = 0 # 현재 위치
    
    for step in case:
        if step == 1:
            currentIdx += 1
        else:
            currentIdx += 2
            currentSize //= 2
    
        if currentIdx >= len(arr):
            break
        currentSize += arr[currentIdx]
    
    if maxSize < currentSize:
        maxSize = currentSize
        
print(maxSize)