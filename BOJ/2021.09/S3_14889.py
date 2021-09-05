'''
스타트와 링크

입력
첫째 줄에 N(4 ≤ N ≤ 20, N은 짝수)이 주어진다. 둘째 줄부터 N개의 줄에 S가 주어진다.
각 줄은 N개의 수로 이루어져 있고, i번 줄의 j번째 수는 Sij 이다. Sii는 항상 0이고, 나머지 Sij는 1보다 크거나 같고, 100보다 작거나 같은 정수이다.

출력
첫째 줄에 스타트 팀과 링크 팀의 능력치의 차이의 최솟값을 출력한다.
'''

'''
- 20C10 = 184756 이므로 각 경우에 대해 완전 탐색을 생각할 수 있다.
* Pass/1st/00:41:04
- 뭔가 좀 오래 걸린 것 같아서 다른 답안도 찾아봤는데 결국 브루트포스 문제였다.
'''
from itertools import combinations

def checkValue(arr, stat, N): # arr에 들어간 거랑 그렇지 않는 것의 차이 리턴
    tempArr = list(arr)
    arr1 = []
    arr2 = []

    sumArr1 = 0
    sumArr2 = 0

    temp = N-1
    while tempArr:
        e = tempArr.pop()
        arr1.append(e)
        for i in range(temp, e, -1):
            arr2.append(i)
        temp = e - 1
    for i in range(temp, -1, -1):
        arr2.append(i)

    for i in range(len(arr1)-1):
        for j in range(i+1, len(arr1)):
            sumArr1 += stat[arr1[i]][arr1[j]]
            sumArr1 += stat[arr1[j]][arr1[i]]
    
    for i in range(len(arr2)-1):
        for j in range(i+1, len(arr2)):
            sumArr2 += stat[arr2[i]][arr2[j]]
            sumArr2 += stat[arr2[j]][arr2[i]]

    return abs(sumArr1-sumArr2)


N = int(input())
stat = []
for i in range(N):
    stat.append(list(map(int, input().split())))
minimum = 10**9

allCase = list(combinations([i for i in range(N)], N//2))
for i in range(len(allCase)//2):
    temp = checkValue(allCase[i], stat, N)
    if minimum > temp:
        minimum = temp

print(minimum)