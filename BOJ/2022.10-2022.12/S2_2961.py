'''
도영이가 만든 맛있는 음식

입력
첫째 줄에 재료의 개수 N(1 ≤ N ≤ 10)이 주어진다.
다음 N개 줄에는 그 재료의 신맛과 쓴맛이 공백으로 구분되어 주어진다.
모든 재료를 사용해서 요리를 만들었을 때, 그 요리의 신맛과 쓴맛은 모두 1,000,000,000보다 작은 양의 정수이다.

출력
첫째 줄에 신맛과 쓴맛의 차이가 가장 작은 요리의 차이를 출력한다. 
'''

'''
- 재료의 개수가 최대 10개까지 뿐이므로 2^10-1의 모든 경우의 수(모두 선택안하는 경우 제외)를 다 확인하도록 한다.
* Pass/1st/00:07:39
'''
from itertools import product

N = int(input())
arr = [] # 각 재료별 (신맛, 쓴맛)의 배열

for i in range(N):
    a, b = map(int, input().split())
    arr.append((a, b))
    
allCase = list(product(range(2), repeat=N))[1:] # 모두 선택 안하는 경우(0, 0, ...)를 제외한 모든 경우의 수
answer = None # 신맛과 쓴맛의 차이 최솟값

for case in allCase:
    tasteProduct = 1 # 신맛의 곱
    tasteSum = 0 # 쓴맛의 합
    
    for idx in range(len(case)):
        if case[idx] == 1:
            tasteProduct *= arr[idx][0]
            tasteSum += arr[idx][1]
            
    if answer == None or answer > abs(tasteProduct - tasteSum):
        answer = abs(tasteProduct - tasteSum)
        
print(answer)
