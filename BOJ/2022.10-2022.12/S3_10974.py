'''
모든 순열

입력
첫째 줄에 N(1 ≤ N ≤ 8)이 주어진다. 

출력
첫째 줄부터 N!개의 줄에 걸쳐서 모든 순열을 사전순으로 출력한다.
'''

'''
- 파이썬의 permutations를 이용하면 쉽게 계산할 수 있다.
* Pass/1st/00:02:52
'''
from itertools import permutations

N = int(input())

allCase = permutations(range(1, N + 1), N)
for case in allCase:
    result = ""
    for e in case:
        result += str(e) + " "
    print(result[:-1])
    