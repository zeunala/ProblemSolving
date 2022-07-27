'''
차집합

입력
첫째 줄에는 집합 A의 원소의 개수 n(A)와 집합 B의 원소의 개수 n(B)가 빈 칸을 사이에 두고 주어진다.
(1 ≤ n(A), n(B) ≤ 500,000)이 주어진다.
둘째 줄에는 집합 A의 원소가, 셋째 줄에는 집합 B의 원소가 빈 칸을 사이에 두고 주어진다.
하나의 집합의 원소는 2,147,483,647 이하의 자연수이며, 하나의 집합에 속하는 모든 원소의 값은 다르다.

출력
첫째 줄에 집합 A에는 속하면서 집합 B에는 속하지 않는 원소의 개수를 출력한다.
다음 줄에는 구체적인 원소를 빈 칸을 사이에 두고 증가하는 순서로 출력한다.
집합 A에는 속하면서 집합 B에는 속하지 않는 원소가 없다면 첫째 줄에 0만을 출력하면 된다.
'''

'''
- 파이썬의 집합 자료형을 이용할 수 있다.
* Fail/1st/00:05:14
'''
import sys

lenA, lenB = map(int, sys.stdin.readline().rstrip().split())
arrA = set(map(int, sys.stdin.readline().rstrip().split()))
arrB = set(map(int, sys.stdin.readline().rstrip().split()))

arrC = list(arrA.difference(arrB))
arrC.sort()
if len(arrC) == 0:
    print(0)
else:
    for i in range(len(arrC)):
        if i != len(arrC) - 1:
            print(arrC[i], end = " ")
        else:
            print(arrC[i])