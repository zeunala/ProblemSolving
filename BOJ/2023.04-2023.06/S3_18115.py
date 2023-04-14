'''
카드 놓기

입력
첫 번째 줄에는 N (1 ≤ N ≤ 10^6)이 주어진다.
두 번째 줄에는 길이가 N인 수열 A가 주어진다. Ai가 x이면, i번째로 카드를 내려놓을 때 x번 기술을 썼다는 뜻이다.
Ai는 1, 2, 3 중 하나이며, An은 항상 1이다.

출력
초기 카드의 상태를 위에서부터 순서대로 출력하여라.
'''

'''
- 첫 번째부터 N, N - 1, ..., 1 순으로 카드를 내려놓아야 한다.
3번 기술을 써서 내려놓는 카드들은 따로 빼서 맨 마지막에 두도록 하면 되며,
카드가 1장일 때는 1번 기술만 쓸 수 있으므로 1번 기술은 반드시 한 번 이상 등장하므로, 우선 처음으로 1번 기술을 쓰는 카드를 맨 앞에 둔다.
맨 앞에 있는 카드가 내려놓이기 전까지 그 뒤에 2번 기술을 쓰는 카드들이 놓여지며,
맨 앞에 있는 카드가 놓여졌다면 그 다음으로 1번 기술을 쓰는 카드가 맨 앞에 오며 처음부터 다시 시작한다.
* Fail/1st/00:27:18/TimeLimitExceeded
'''
import sys

N = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

answerFront = []
answerBack = []

# 3번 기술을 쓰는 것들을 뒤로 빼낸다.
for i in range(N):
    if arr[i] == 3:
        answerBack.append(N - i)

i = 0
while i < N:
    # 1번 기술을 처음으로 쓴 카드를 맨 앞에 둔다.
    firstIdx = arr[i:].index(1) + i
    answerFront.append(N - firstIdx)

    # 2번 기술을 쓴 나머지 카드들을 그 카드 뒤에 놓는다.
    for i in range(i, firstIdx):
        if arr[i] == 2:
            answerFront.append(N - i)
            
    i = firstIdx + 1

# 3번 기술을 쓴 카드들을 뒤집어 뒤에 놓는다. (먼저 3번 기술을 쓴 카드가 맨 뒤에 위치해야 하기 때문이다)
answerFront.extend(list(reversed(answerBack)))

for e in answerFront:
    print(e, end = " ")