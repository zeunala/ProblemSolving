'''
기념품

입력
첫째 줄에 BOJ 캠프 참가자의 수 N (1 ≤ N ≤ 5,000)이 주어진다.

출력
첫째 줄에 기념품을 받는 사람이 입고 있는 티셔츠의 번호를 출력한다.
'''

'''
- 문제의 요구사항을 그대로 구현한다. 배열을 이용하여 각 단계마다 사람을 제거해나간다.
* Pass/1st/00:11:53
'''
N = int(input())
arr = [i for i in range(1, N + 1)]

currentLevel = 1 # 단계
currentPos = 0 # 현재 arr[i]에 위치할 경우의 i값

while len(arr) > 1:
    currentPos = (currentPos + (currentLevel ** 3 - 1)) % len(arr) # t레벨 기준 t^3 - 1칸 이동(현재 위치한 사람부터 하나이므로)
    arr.pop(currentPos) # 앞에 있는 사람 게임에서 제외
    
    currentLevel += 1

print(arr[0])