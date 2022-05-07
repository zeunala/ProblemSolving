'''
역사

입력
첫째 줄에 첫 줄에 사건의 개수 n(400 이하의 자연수)과 알고 있는 사건의 전후 관계의 개수 k(50,000 이하의 자연수)가 주어진다.
다음 k줄에는 전후 관계를 알고 있는 두 사건의 번호가 주어진다.
이는 앞에 있는 번호의 사건이 뒤에 있는 번호의 사건보다 먼저 일어났음을 의미한다.
물론 사건의 전후 관계가 모순인 경우는 없다.
다음에는 사건의 전후 관계를 알고 싶은 사건 쌍의 수 s(50,000 이하의 자연수)이 주어진다.
다음 s줄에는 각각 서로 다른 두 사건의 번호가 주어진다. 사건의 번호는 1보다 크거나 같고, N보다 작거나 같은 자연수이다.

출력
s줄에 걸쳐 물음에 답한다.
각 줄에 만일 앞에 있는 번호의 사건이 먼저 일어났으면 -1, 뒤에 있는 번호의 사건이 먼저 일어났으면 1,
어떤지 모르면(유추할 수 없으면) 0을 출력한다.
'''

'''
- 각 사건에 대하여 뒤에 있는 번호의 사건들의 리스트를 저장하는 식으로 해보자.
* Fail/1st/00:16:37
- 코드 중간에서 오류를 발견하여 수정하였다.
* Fail/2nd/00:23:09/TimeOver
'''
import sys

def dfsAfter(after, current, target, visited): # current 이후 target이 일어났는지 여부 리턴
    if visited[current]:
        return False
    else:
        visited[current] = True
    
    for e in after[current]:
        if target == e:
            return True
        elif not visited[e]:
            if dfsAfter(after, e, target, visited):
                return True
    
    return False
    

N, K = map(int, sys.stdin.readline().rstrip().split())

after = [[] for _ in range(N+1)] # after[i]는 i번 사건보다 나중에 일어난 사건들의 번호가 담긴다.

for i in range(K):
    first, second = map(int, sys.stdin.readline().rstrip().split())
    after[first].append(second)

S = int(sys.stdin.readline().rstrip())

for i in range(S):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    
    if dfsAfter(after, a, b, [False for _ in range(N+1)]):
        print(-1)
    elif dfsAfter(after, b, a, [False for _ in range(N+1)]):
        print(1)
    else:
        print(0)