'''
입력
N값이 첫 번째 줄에 입력된다. (1 ≤ N < 100,000, N은 홀수)
주언이가 받은 카드 N장에 적힌 수들이 두 번째 줄에 입력된다.
사장님이 받은 카드 N장에 적힌 수들이 세 번째 줄에 입력된다. 

출력
주언이가 이길 확률이 조금이라도 있을 경우 “YES” 라고 출력하고,
주언이가 이길 확률이 존재하지 않을 경우 “NO”라고 출력한다.
'''

'''
- 주언이가 작은 수부터 내면 사장은 그보다 큰 수 중 최솟값을 내도록 한다. (N+1)/2번까지 반복할 수 있다면 YES, 아니면 NO를 출력한다.
* Fail/1st/00:13:17/IndexError
'''
import sys
N = int(input())
arr1 = list(map(int, sys.stdin.readline().rstrip().split())) # 주언이 카드
arr2 = list(map(int, sys.stdin.readline().rstrip().split())) # 사장 카드
answer = "YES"

arr1.sort()
arr2.sort()

arr2Idx = -1 # 0부터 시작하기 위함
for i in range((N+1)//2):
    targetNumber = arr1[i] # 주언이가 낸 수
    arr2Idx += 1
    
    while arr2[arr2Idx] <= targetNumber:
        arr2Idx += 1
        if arr2Idx >= len(arr2): # 사장이 더 큰 수를 낼 수 없는 경우
            answer = "NO"
            break
        
    if answer == "NO":
        break

print(answer)