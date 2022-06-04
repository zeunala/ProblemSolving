'''
연속합

입력
첫째 줄에 정수 n(1 ≤ n ≤ 100,000)이 주어지고 둘째 줄에는 n개의 정수로 이루어진 수열이 주어진다.
수는 -1,000보다 크거나 같고, 1,000보다 작거나 같은 정수이다.

출력
첫째 줄에 답을 출력한다.
'''

'''
- 분할 정복 알고리즘을 이용해보자. 가운데를 기준으로 왼쪽끼리만 / 오른쪽끼리만 / 가운데 끼는 경우 셋을 생각한다.
* Pass/1st/00:11:46
'''
import sys

def findMax(arr):
    if len(arr) == 1:
        return arr[0]
    elif len(arr) == 0:
        return -(10 ** 15)
    
    middleIdx = len(arr) // 2
    
    caseA = findMax(arr[:middleIdx]) # 왼쪽에서 최대가 되는 경우
    caseB = findMax(arr[middleIdx + 1:]) # 오른쪽에서 최대가 되는 경우
    
    # 가운데를 끼는 경우
    leftMax = 0
    leftCurrent = 0
    for idx in range(middleIdx - 1, -1, -1):
        leftCurrent += arr[idx]
        if leftCurrent > leftMax:
            leftMax = leftCurrent
    rightMax = 0
    rightCurrent = 0
    for idx in range(middleIdx + 1, len(arr)):
        rightCurrent += arr[idx]
        if rightCurrent > rightMax:
            rightMax = rightCurrent
    
    caseC = arr[middleIdx] + leftMax + rightMax
    
    return max(caseA, caseB, caseC)
    
n = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
print(findMax(arr))