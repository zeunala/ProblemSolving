'''
오셀로 재배치

입력
입력 데이터는 표준 입력을 사용한다. 입력은 T개의 테스트 데이터로 구성된다.
각 입력의 첫 번째 줄에는 오셀로 말의 개수 N(1 ≤ N ≤ 100,000)이 주어진다.
각 입력의 두 번째 줄과 세 번째 줄에는 각각 오셀로 말의 초기 상태와 목표 상태가 주어진다.
초기 상태와 목표 상태의 말의 개수는 항상 N과 일치한다. 흰색 면이 보이는 경우에는 W, 검은색 면이 보이는 경우에는 B로 주어진다.

출력
출력은 표준 출력을 사용한다. 입력받은 데이터에 대해, 한 줄에 1개씩 초기 상태에서 목표 상태를 만들기 위한 작업의 최소 횟수를 구한다.
'''

'''
- 우선 초기 상태와 목표 상태의 검정/흰색의 개수가 일치할 때까지 말 1개를 뒤집어 색상을 바꿔야한다.
검정/흰색 개수를 일치해야만 목표 상태로 만들수 있고 그러기 위해서는 말 1개를 뒤집는 방법밖에 없기 때문이다.
이후 검정/흰색 개수가 같아진다면 초기 상태와 목표 상태가 색깔이 다른게 n개라면 n/2번 말의 위치를 바꿔주면 최소 횟수로 만들 수 있다.
* Pass/1st/00:11:10
'''
import sys

T = int(sys.stdin.readline().rstrip())

for testcase in range(T):
    N = int(sys.stdin.readline().rstrip())
    startStatus = list(sys.stdin.readline().rstrip())
    targetStatus = list(sys.stdin.readline().rstrip())
    
    needColorChange = abs(startStatus.count("B") - targetStatus.count("B")) # B, W의 개수를 맞추기 위해 뒤집어야 하는 수
    
    differentColorCount = 0 # 초기 상태와 목표 상태간의 색깔 다른 개수
    for i in range(N):
        if startStatus[i] != targetStatus[i]:
            differentColorCount += 1
    
    # 우선 뒤집기로 B, W의 개수를 맞추고, 그래도 색깔이 다른게 있다면 다른 개수의 절반만큼 위치 교환을 해주면 된다. 
    answer = needColorChange + (differentColorCount - needColorChange) // 2
    
    print(answer)