'''
차트

입력
첫째 줄에 N이 주어진다. N은 1보다 크거나 같고, 8보다 작거나 같다.
둘째 줄에, 민식이가 조사한 개의 수가 주어진다.
개의 수는 100 이하의 자연수이고, 조사한 개의 수의 합은 항상 100이다.

출력
첫째 줄에 정답을 출력한다.
'''

'''
- N의 개수가 8이하이므로 모든 경우의 수를 체크하도록 한다.
8개를 무작위로 배치하고 각 경우에 대하여 원의 중심을 지나는 선의 개수를 구한다.
이때 원의 중심을 지나는 선의 개수는 연속된 수를 더했을 때 50이 나오는 경우로, 다만 마지막 수는 제외해야 같은 경우를 중복해서 세지 않게 된다.
예를 들어 10 40 10 40은 [10 40] 10 40, 10 [40 10] 40의 2가지이며,
1 48 1 1 48 1 은 [1 48 1] 1 48 1, 1 [48 1 1] 48 1, 1 49 [1 1 48] 1의 3가지이다.
(주어진 수의 합이 항상 100이기 때문에 이러한 방법이 가능하다)
* Pass/1st/00:13:15
'''
from itertools import permutations

def getMaxLine(arr):
    arr.pop() # 마지막은 고려하지 않음
    result = 0
    
    for i in range(len(arr)):
        currentSum = 0
        for j in range(i, len(arr)):
            currentSum += arr[j]
            
            if currentSum == 50:
                result += 1
                break
            
            if currentSum > 50:
                break
            
    return result

N = int(input())
arr = list(map(int, input().split()))
answer = 0

for case in permutations(range(N), r = N):
    # arr을 무작위로 배치
    tempArr = [0] * N
    for i in range(len(case)):
        tempArr[i] = arr[case[i]]
        
    tempAnswer = getMaxLine(tempArr)
    if tempAnswer > answer:
        answer = tempAnswer
        
print(answer)