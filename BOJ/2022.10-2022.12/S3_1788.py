'''
피보나치 수의 확장

입력
첫째 줄에 n이 주어진다. n은 절댓값이 1,000,000을 넘지 않는 정수이다.

출력
첫째 줄에 F(n)이 양수이면 1, 0이면 0, 음수이면 -1을 출력한다.
둘째 줄에는 F(n)의 절댓값을 출력한다.
이 수가 충분히 커질 수 있으므로, 절댓값을 1,000,000,000으로 나눈 나머지를 출력한다.
'''

'''
- F(n)을 절댓값이 1인 경우부터 구해나간다.
* Fail/1st/00:24:14/IndexError
'''
n = int(input())
plusF = [0, 1] # plusF[i]는 F(i)를 가리킴
minusF = [0, 1] # minusF[i]는 F(-i)를 가리킴

for i in range(2, 1000000):
    nextPlus = (plusF[i - 2] + plusF[i - 1]) % 1000000000
    nextMinus = abs(minusF[i - 2] - minusF[i - 1]) % 1000000000
    if minusF[i - 2] - minusF[i - 1] < 0:
        nextMinus *= -1
    plusF.append(nextPlus)
    minusF.append(nextMinus)
    
answer = 0
if n >= 0:
    answer = plusF[n]
else:
    answer = minusF[-n]
    
if answer > 0:
    print(1)
elif answer < 0:
    print(-1)
else:
    print(0)
    
print(abs(answer))