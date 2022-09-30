'''
사이클 게임

입력
입력은 표준입력을 사용한다. 입력의 첫 번째 줄에는 점의 개수를 나타내는 정수 3 ≤ n ≤ 500,000 과
진행된 차례의 수를 나타내는 정수 3 ≤ m ≤ 1,000,000 이 주어진다.
게임에서 사용하는 n개의 점에는 0 부터 n − 1 까지 고유한 번호가 부여되어 있으며, 이 중 어느 세 점도 일직선 위에 놓이지 않는다.
이어지는 m 개의 입력 줄에는 각각 i번째 차례에 해당 플레이어가 선택한 두 점의 번호가 주어진다 (1 ≤ i ≤ m).

출력
출력은 표준출력을 사용한다. 입력으로 주어진 케이스에 대해,
m 번째 차례까지 게임을 진행한 상황에서 이미 게임이 종료되었다면 사이클이 처음으로 만들어진 차례의 번호를 양의 정수로 출력하고,
m 번의 차례를 모두 처리한 이후에도 종료되지 않았다면 0을 출력한다.
'''

'''
- 각 점마다 parent 변수를 두고, 번호가 적은걸 부모로 하여 연결한다.
만약 parent가 같은 두 점을 연결하려고 하면 그 순간 사이클이 만들어진 것이다.
* Fail/1st/00:11:08
- 잘못 작성한 부분을 수정하였고 추가로 최적화과정도 추가하였다.
* Fail/2nd/00:15:42
- 2 3 / 2 4 / 1 4 / 1 2 같은 반례를 막도록 parentArr 갱신 코드를 수정하였다.
* Pass/3rd/00:37:56
'''
import sys

def findParent(parentArr, i): # i번의 parent를 찾는다.
    while i != parentArr[i]:
        i = parentArr[i]
    return parentArr[i]

def union(parentArr, i, j): # i번 점과 j번 점을 합치고 사이클 유무를 리턴한다.
    parentArr[i] = findParent(parentArr, i)
    parentArr[j] = findParent(parentArr, j)
    
    if parentArr[i] == parentArr[j]: # 이미 같은 부모, 즉 사이클 형성되는 경우
        return True
    else:
        if i < j: # i가 부모
            parentArr[parentArr[j]] = parentArr[i]
        else: # j가 부모
            parentArr[parentArr[i]] = parentArr[j]
        
        return False

n, m = map(int, sys.stdin.readline().rstrip().split()) # n: 점의 개수, m: 차례의 개수
parentArr = [i for i in range(n)]

answer = 0

for i in range(1, m + 1):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    
    if answer == 0: # 중간에 사이클이 나오지 않은 경우만 체크
        if union(parentArr, a, b):
            answer = i

print(answer)