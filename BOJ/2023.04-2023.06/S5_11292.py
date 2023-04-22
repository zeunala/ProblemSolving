'''
키 큰 사람

입력
입력은 여러개의 테스트케이스로 구성되어있다.
각 테스트케이스는 첫 번째 줄에 학생의 수 N (0 < N ≤ 50)이 주어지고,
이어서 N개의 줄에 각 학생의 이름과 키가 공백으로 구별되어 주어진다.
학생의 이름은 알파벳 대/소문자로만 이루어져 있고, 길이는 10을 넘지 않는다.
학생의 키는 소숫점 이하 2자리까지 주어진다. N이 0으로 주어지는 경우 프로그램을 종료한다.

출력
각 테스트케이스에 대해, 가장 키가 큰 학생의 이름을 한 줄에 출력한다.
같은 키의 사람이 여러명 일 경우 모두 출력해야 하며, 순서는 입력으로 들어온 순서를 유지해야 한다.
'''

'''
- 문제의 요구사항을 그대로 구현하면 된다.
* Pass/1st/00:04:34
'''
import sys

while True:
    N = int(sys.stdin.readline().rstrip())
    if N == 0:
        break
    
    arr = [] # (이름, 키)의 배열
    for i in range(N):
        a, b = sys.stdin.readline().rstrip().split()
        b = float(b)
        arr.append((a, b))

    maxValue = max([e[1] for e in arr]) # 키의 최댓값
    
    for (a, b) in arr: # 입력 순서대로 돌며 키가 최댓값인 경우 출력
        if b == maxValue:
            print(a, end = " ")
    print()