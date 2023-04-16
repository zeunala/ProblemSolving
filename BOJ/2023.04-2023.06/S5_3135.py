'''
라디오

입력
첫 줄엔 정수 A와 B가 주어진다 (1 ≤ A, B < 1000, A ≠ B).
다음 줄엔 정수 N이 주어진다 (1 ≤ N ≤ 5).
다음 N개의 줄엔 미리 지정되어 있는 주파수가 주어진다 (주파수는 1000 보다 작다).

출력
주파수 A에서 B로 갈 때 눌러야 하는 버튼수의 최솟값을 출력한다.
'''

'''
- 출발지와 즐겨찾기의 모든 주파수 ~ 목적 주파수까지의 거리 중 최솟값을 구하면 된다.
이때 즐겨찾기로 갈 경우 버튼 1번이 추가된다.
* Pass/1st/00:03:29
'''
A, B = map(int, input().split())
N = int(input())
arr = []

for i in range(N):
    arr.append(int(input()))
    
answer = abs(A - B)
for e in arr:
    tempAnswer = abs(e - B) + 1
    answer = min(answer, tempAnswer)

print(answer)