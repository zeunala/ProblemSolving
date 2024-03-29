'''
점수 계산

입력
8개 줄에 걸쳐서 각 문제에 대한 참가자의 점수가 주어진다.
점수는 0보다 크거나 같고, 150보다 작거나 같다.
모든 문제에 대한 점수는 서로 다르다.
입력으로 주어지는 순서대로 1번 문제, 2번 문제, ... 8번 문제이다.

출력
첫째 줄에 참가자의 총점을 출력한다.
둘째 줄에는 어떤 문제가 최종 점수에 포함되는지를 공백으로 구분하여 출력한다.
출력은 문제 번호가 증가하는 순서이어야 한다.
'''

'''
- 문제의 요구사항을 그대로 구현하면 되는 문제이다.
* Pass/1st/00:05:13
- 백준의 시스템상 마지막 공백은 무시하는 것으로 보인다.
'''
arr = [] # (점수, 문제번호)의 튜플의 배열
for i in range(1, 9):
    arr.append((int(input()), i))
    
arr.sort(key = lambda x : (-x[0], x[1])) # 점수 오름차순, 같으면 문제번호 내림차순
top5 = [arr[0][1], arr[1][1], arr[2][1], arr[3][1], arr[4][1]] # 점수가 가장 높은 5개의 문제번호
top5.sort()
score = arr[0][0] + arr[1][0] + arr[2][0] + arr[3][0] + arr[4][0]

print(score)
for e in top5:
    print(e, end = " ")
