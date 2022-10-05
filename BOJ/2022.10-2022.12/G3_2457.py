'''
공주님의 정원

입력
첫째 줄에는 꽃들의 총 개수 N (1 ≤ N ≤ 100,000)이 주어진다.
다음 N개의 줄에는 각 꽃이 피는 날짜와 지는 날짜가 주어진다.
하나의 날짜는 월과 일을 나타내는 두 숫자로 표현된다.
예를 들어서, 3 8 7 31은 꽃이 3월 8일에 피어서 7월 31일에 진다는 것을 나타낸다. 

출력
첫째 줄에 선택한 꽃들의 최소 개수를 출력한다. 만약 두 조건을 만족하는 꽃들을 선택할 수 없다면 0을 출력한다.
'''

'''
- 우선 월/일을 숫자로 변환시킨 후, 꽃이 없는 날이 없도록 하면서 가장 늦게 지는 꽃을 그리디 알고리즘으로 선택한다.
* Fail/1st/00:26:10
'''
import sys

def monthDayToNum(month, day): # 1월 1일을 1로 하여 몇 번째 날인지 리턴
    arr = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    result = 0
    for i in range(1, month + 1):
        if i < month:
            result += arr[i]
            continue
        else:
            result += day
            return result

        
N = int(sys.stdin.readline().rstrip())
arr = [] # (피는 날짜, 지기 직전의 날짜)의 튜플 저장

for i in range(N):
    a, b, c, d = map(int, sys.stdin.readline().rstrip().split())
    arr.append((monthDayToNum(a, b), monthDayToNum(c, d) - 1))
    
arr.sort(key = lambda x : x[0], reverse = True) # 빨리 피는 게 스택의 끝에 오도록 정렬
today = monthDayToNum(3, 1) # 아무리 늦어도 이 때까지는 꽃이 새로 피어야하는 날짜
answer = 0

while arr and today < monthDayToNum(12, 1):
    currentStack = [] # 꽃을 선택하는 후보군들의 목록. 꽃이 피어야 하는 상황일 경우 여기서 가장 늦게 피는 꽃을 고른다.
    
    while arr and arr[-1][0] <= today:
        currentStack.append(arr.pop())
    
    if len(currentStack) == 0: # 시간이 되었는데 꽃을 선택할 후보가 없는 경우 해가 없음
        answer = 0
        break
    
    answer += 1
    today = max([currentStack[i][1] for i in range(len(currentStack))]) + 1 # 현재 후보군 중 가장 늦게 지는 꽃을 선택함
    
print(answer)