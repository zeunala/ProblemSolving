'''
1, 2, 3 더하기 2

입력
첫째 줄에 정수 n과 k가 주어진다. n은 양수이며 11보다 작고, k는 2^31-1보다 작거나 같은 자연수이다.

출력
n을 1, 2, 3의 합으로 나타내는 방법 중에서 사전 순으로 k번째에 오는 것을 출력한다. k번째 오는 식이 없는 경우에는 -1을 출력한다.
'''

'''
- n의 범위가 10이하이므로 모든 경우의 수를 다 구하고 정렬하도록 한다.
* Pass/1st/00:14:01
'''
allCase = [[] for _ in range(11)] # allCase[n]은 n을 1, 2, 3의 합으로 나타내는 모든 경우의 수들을 나타낸다.

allCase[1].extend([(1,)])
allCase[2].extend([(1, 1), (2,)])
allCase[3].extend([(1, 1, 1), (1, 2), (2, 1), (3,)])
for i in range(4, 11):
    # 1 + allCase[i - 1], 2 + allCase[i - 2], 3 + allCase[i - 3]의 경우의 수가 가능하다.
    allCase[i].extend([(1, ) + e for e in allCase[i - 1]])
    allCase[i].extend([(2, ) + e for e in allCase[i - 2]])
    allCase[i].extend([(3, ) + e for e in allCase[i - 3]])
    
n, k = map(int, input().split())

if len(allCase[n]) < k:
    print(-1)
else:
    result = ""
    for e in allCase[n][k - 1]:
        result += str(e) + "+"
    print(result[:-1])