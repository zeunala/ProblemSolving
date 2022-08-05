'''
K번째 수

입력
첫째 줄에 N(1 ≤ N ≤ 5,000,000)과 K (1 ≤ K ≤ N)이 주어진다.
둘째에는 A1, A2, ..., AN이 주어진다. (-10^9 ≤ Ai ≤ 10^9)

출력
A를 정렬했을 때, 앞에서부터 K번째 있는 수를 출력한다.
'''

'''
- 퀵 소트 때와 비슷하게 임의의 수 하나를 잡고 그 수보다 작은 그룹과 큰 그룹으로 묶는다.
* Fail/1st/00:20:27
'''
import sys

def findIndex(arr, n): # 배열 arr에서 n번째로 큰 수를 찾는다.
    if len(arr) == 1:
        return arr[0]
    
    target = arr[0] # 첫번째 수를 기준으로
    arrSmall = [] # 그 수보다 작은 그룹과
    arrBig = [] # 그 수보다 큰 그룹으로 나눈다.
    
    for i in range(1, len(arr)):
        if target > arr[i]:
            arrSmall.append(arr[i])
        else:
            arrBig.append(arr[i])
        
    if n > len(arrSmall) and len(arr) - n >= len(arrBig): # arr의 첫번째 수가 마침 n번째로 큰 수였다면 그걸 바로 리턴
        return target
    elif n <= len(arrSmall):
        return findIndex(arrSmall, n)
    else:
        return findIndex(arrBig, n - (len(arr) - len(arrBig)))
    

N, K = map(int, sys.stdin.readline().rstrip().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
print(findIndex(arr, K))