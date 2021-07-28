'''
문자열 제곱

입력
입력은 10개 이하의 테스트 케이스로 이루어져 있다. 각각의 테스트 케이스는 s를 포함한 한 줄로 이루어져 있다. s의 길이는 적어도 1이며, 백만글자를 넘지 않는다. 마지막 테스트 케이스의 다음 줄은 마침표이다.

출력
각각의 테스트 케이스에 대해, s=a^n을 만족하는 가장 큰 n을 찾은 뒤 출력한다.
'''

'''
- n는 반드시 s의 길이의 약수가 될 수 밖에 없으므로, s의 길이가 100만이 안된다고 했으므로 s의 약수의 개수는 2000개를 넘지 않을 것이다.
따라서 n의 모든 경우의 수를 구해보고 각각의 n에 대해 같은지 찾아볼 수 있겠다.
* Pass/1st/00:38:03
'''
import math
import time

def findCase(n): # n의 모든 약수를 찾아 내림차순으로 정렬 후 반환
    result = []
    for i in range(1, int(math.sqrt(n))+1):
        if n%i==0:
            result.append(i)
            if(i!=n//i):
                result.append(n//i)

    result.sort(reverse=True) # 내림차순으로 정렬
    return result

answer = []
while True:
    command = input()
    if command == ".":
        break

    commandLen = len(command)
    commandCase = findCase(commandLen) # 입력받은 문자열의 약수들을 담음

    n = 0
    for e in commandCase:
        if command == (command[:commandLen//e]*e):
            n = e
            break
    answer.append(n)

for e in answer:
    print(e)