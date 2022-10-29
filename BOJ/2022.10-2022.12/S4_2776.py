'''
암기왕

입력
첫째 줄에 테스트케이스의 개수 T가 들어온다.
다음 줄에는 ‘수첩 1’에 적어 놓은 정수의 개수 N(1 ≤ N ≤ 1,000,000)이 입력으로 들어온다.
그 다음 줄에  ‘수첩 1’에 적혀 있는 정수들이 N개 들어온다. 그 다음 줄에는 ‘수첩 2’에 적어 놓은 정수의 개수 M(1 ≤ M ≤ 1,000,000) 이 주어지고, 다음 줄에 ‘수첩 2’에 적어 놓은 정수들이 입력으로 M개 들어온다. 모든 정수들의 범위는 int 로 한다.

출력
‘수첩2’에 적혀있는 M개의 숫자 순서대로, ‘수첩1’에 있으면 1을, 없으면 0을 출력한다.
'''

'''
- 파이썬의 set을 이용하면 쉽게 계산할 수 있다.
* Fail/1st/00:04:37
- 테스트케이스 수에 대한 코드를 빠뜨려서 수정하였다.
* Pass/2nd/00:10:56
'''
import sys

T = int(sys.stdin.readline().rstrip())

for case in range(T):
    arrLen1 = int(sys.stdin.readline().rstrip())
    arr1 = set(map(int, sys.stdin.readline().rstrip().split()))
    arrLen2 = int(sys.stdin.readline().rstrip())
    arr2 = list(map(int, sys.stdin.readline().rstrip().split()))
    for e in arr2:
        if e in arr1:
            print(1)
        else:
            print(0)