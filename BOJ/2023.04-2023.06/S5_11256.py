'''
사탕

입력
첫 번째 줄에는 테스트 케이스의 개수 T (1 ≤ T ≤ 10)가 주어진다. 각각의 테스트 케이스는 아래 형식을 따른다.
테스트 케이스의 첫 번째 줄에는 사탕의 개수 J와 상자의 개수 N이 주어진다. (1 ≤ J, N ≤ 1,000)
다음 N개의 줄에는 각각 줄마다 i번째 상자의 세로 길이 Ri 그리고 가로 길이 Ci가 주어진다.
상자의 크기는 다른 상자의 크기와 똑같을 수도 있다. 상자에는 Ri * Ci보다 더 많은 사탕을 포장할 수 없다. (1 ≤ Ri, Ci ≤ 10,000)

출력
출력은 T개의 줄로 이루어진다. 각각의 줄마다 i번째 테스트 케이스에서 최소한의 상자 개수를 출력하여야 한다.
'''

'''
- 그리디 알고리즘을 이용하여 상자 크기가 큰 상자부터 차례로 담으면 된다.
* Pass/1st/00:04:12
'''
import sys

T = int(sys.stdin.readline().rstrip())
for i in range(T):
    J, K = map(int, sys.stdin.readline().rstrip().split())
    currentCandy = J # 남은 사탕 수
    boxArr = []
    
    for i in range(K):
        R, C = map(int, sys.stdin.readline().rstrip().split())
        boxArr.append(R * C)
    boxArr.sort(reverse=True)
    
    answer = 0
    while currentCandy > 0:
        currentCandy -= boxArr[answer]
        answer += 1
    print(answer)