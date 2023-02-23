'''
관중석

입력
첫 줄에 원의 반지름 D1과 D2가 양의 정수로 주어진다. 단, 1 ≤ D1 ≤ D2 ≤ 2,000이다.

출력
사용되는 좌석의 수를 나타내는 하나의 양의 정수를 출력한다. 
'''

'''
- 좌석을 0이상 1미만의 기약분수로 나타내고, 서로 다른 여러 개의 좌석의 개수를 세면 된다.
예를 들어 D가 3일 때는 0/3, 1/3, 2/3으로 나타낼 수 있으며,
D가 6일 때는 0/6, 1/6, 2/6, 3/6, 4/6, 5/6으로 나타낼 수 있다.
서로 다른 분수의 개수를 모두 세면 된다. 즉 1/3과 2/6같은 중복은 하나만 센다.
* Fail/1st/00:09:52
- 마지막 서브태스크를 통과하지 못해 최적화가 필요해보인다.
모든 경우의 수를 저장하지 말고, 그냥 약분이 되는 상황에서 분모가 D1~D2 범위안에 있으면 총 개수에 포함을 시키지 않으면 된다.
그리고 약분이 됨에도 총 개수에 포함되는 것들만 따로 모으면 된다. 예를 들어 D가 4~6일 때 2/4와 3/6 모두 세면 안되기 때문이다.
* Fail/2nd/00:28:26
- 최적화가 잘못된 부분이 있어 수정하였다.
* Fail/3rd/00:40:44
'''
import math

def getDivTuple(a, b): # a/b의 분수를 약분해서 (a, b)의 형태로 반환
    gcdAB = math.gcd(a, b)
    return (a // gcdAB, b // gcdAB)

D1, D2 = map(int, input().split())
answer = 1 # 0인 지점을 미리 하나 센다.
otherCase = set()

for i in range(D1, D2 + 1):
    for j in range(1, i):
        # j / i 꼴의 분수가 나오는데, 약분했을 때 분모가 D1~D2가 아니면 총 개수가 합산한다.
        tempResult = getDivTuple(j, i)
        
        if tempResult[1] != i:
            # i는 D2안에 있으므로 D2와 비교할 필요는 없다.
            if tempResult[1] >= D1 or tempResult in otherCase:
                continue
            otherCase.add(tempResult)
        answer += 1
        
print(answer)