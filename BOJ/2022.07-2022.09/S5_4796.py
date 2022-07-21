'''
캠핑

입력
입력은 여러 개의 테스트 케이스로 이루어져 있다.
각 테스트 케이스는 한 줄로 이루어져 있고, L, P, V를 순서대로 포함하고 있다.
모든 입력 정수는 int범위이다. 마지막 줄에는 0이 3개 주어진다.

출력
각 테스트 케이스에 대해서, 강산이가 캠핑장을 최대 며칠동안 사용할 수 있는지 예제 출력처럼 출력한다.
'''

'''
- 문제의 조건을 그대로 구현하도록 한다.
* Pass/1st/00:04:18
'''
testIdx = 0
while True:
    testIdx += 1
    a, b, c = map(int, input().split())
    
    if a == 0 and b == 0 and c == 0:
        break
    
    answer = (c // b) * a + min(c % b, a)
    print("Case " + str(testIdx) + ": " + str(answer))