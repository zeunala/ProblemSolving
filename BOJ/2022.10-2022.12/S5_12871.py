'''
무한 문자열

입력
첫째 줄에 s, 둘째 줄에 t가 주어진다. 두 문자열 s와 t의 길이는 50보다 작거나 같은 자연수이고, 알파벳 소문자로만 이루어져 있다. 

출력
첫째 줄에 f(s)와 f(t)가 같으면 1을, 다르면 0을 출력한다.
'''

'''
- 문자열의 크기가 50까지밖에 안되므로 그냥 길이를 맞춰서(최소공배수) 같은지를 비교한다.
* Pass/1st/00:03:48
'''
import math

s = input()
t = input()

newS = s * (len(t) // math.gcd(len(s), len(t)))
newT = t * (len(s) // math.gcd(len(s), len(t)))

if newS == newT:
    print(1)
else:
    print(0)