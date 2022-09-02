'''
방 번호

입력
첫째 줄에 다솜이의 방 번호 N이 주어진다. N은 1,000,000보다 작거나 같은 자연수이다.

출력
첫째 줄에 필요한 세트의 개수를 출력한다.
'''

'''
- 딕셔너리를 이용하여 0~9의 각 등장 횟수를 기록해서 최댓값을 출력하도록 한다. 이 때 6과 9에 주의한다.
* Fail/1st/00:05:54
- 6과 9의 균형을 맞추는 부분의 코드를 수정하였다.
* Pass/2nd/00:07:39
'''
from collections import defaultdict

inputString = input()
numDict = defaultdict(int)

for e in inputString:
    numDict[e] += 1
    
while numDict['6'] < numDict['9']: # 6과 9의 균형을 맞춘다.
    numDict['6'] += 1
    numDict['9'] -= 1

while numDict['9'] < numDict['6']: # 6과 9의 균형을 맞춘다.
    numDict['9'] += 1
    numDict['6'] -= 1

print(max(numDict.values()))