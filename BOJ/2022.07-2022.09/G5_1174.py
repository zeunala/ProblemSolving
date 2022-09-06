'''
줄어드는 수

입력
N이 주어진다. N은 1,000,000보다 작거나 같은 자연수이다.

출력
첫째 줄에 N번째 작은 줄어드는 수를 출력한다.
'''

'''
- 9876543210의 부분문자열(연속일 필요성X)들을 크기 순으로 나열하도록 한다.
* Fail/1st/00:08:48
- 문자열을 뽑을 때 최대 10개까지 뽑을 수 있도록 수정하였다.
* Pass/2nd/00:10:20
'''
from itertools import combinations

N = int(input())

num = "9876543210"
arr = [-1]

for i in range(1, 11):
    tempArr = []
    
    for e in list(combinations("9876543210", i)): # 예를 들어 i = 2라면 e는 ('9', '7') 같은 식이 됨
        tempElement = ""
        for f in e: # ('9', '7')을 97과 같은 형태로 만들어줌
            tempElement += f
        tempArr.append(int(tempElement))
    
    tempArr.sort()
    arr.extend(tempArr)

if N >= len(arr):
    print(-1)
else:
    print(arr[N])