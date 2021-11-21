'''
도미노 예측

입력
첫 번째 줄에 숫자 도미노의 개수 N과 질문의 수 Q가 정수로 주어진다. (3 ≤ N ≤ 2 × 10^5, 1 ≤ Q ≤ 10^5)
두 번째 줄에 사장님이 기록한 N-1개의 정수가 주어진다. (각각의 정수는 0 이상 2^31-1 이하이다.)
세 번째 줄부터 Q개의 줄에 걸쳐 각각의 줄에 사장님의 질문이 주어진다.
질문의 형식은 “0 x y” 또는 “1 x y d”이고, 순서대로 1번 질문과 2번 질문을 의미한다. ( 1 ≤ x ≤ y ≤ N, 0 ≤ d ≤ 2^31-1)

출력
주어진 질문의 답을 Q개의 줄에 걸쳐 출력한다.
'''

'''
- (a^b)^(b^c)=a^c, x^y = (a^x)^(a^y), a^(a^b)=b를 이용하여 질문들을 해결할 수 있다.
* Pass/1st/00:26:18
'''
import sys

N, Q = map(int, input().split())
arr = list(map(int, sys.stdin.readline().rstrip().split())) # arr[i]는 i번째 수와 i+1번째 수를 XOR한 값
arr2 = [arr[0]] # arr2[i]는 arr[0], arr[1], ..., arr[i]를 모두 XOR한 값. 이는 첫번째 수와 i+1번째 수를 XOR한 값과 같다.
for i in range(1, len(arr)):
    arr2.append(arr2[i-1] ^ arr[i]) ## a XOR b 는 a ^ b로 계산가능하다.

question = []    
for i in range(Q):
    question.append(list(map(int, sys.stdin.readline().rstrip().split())))
    
for i in range(Q):
    if question[i][0] == 0:
        if question[i][1] == question[i][2]:
            print(0) # a ^ a = 0
        elif question[i][1] == 1:
            print(arr2[question[i][2] - 2])
        else:
            print(arr2[question[i][1] - 2] ^ arr2[question[i][2] - 2])
    else:
        xorValue = 0
        if question[i][1] == question[i][2]:
            xorValue = 0
        elif question[i][1] == 1:
            xorValue = arr2[question[i][2] - 2]
        else:
            xorValue = arr2[question[i][1] - 2] ^ arr2[question[i][2] - 2]
        print(question[i][3] ^ xorValue)