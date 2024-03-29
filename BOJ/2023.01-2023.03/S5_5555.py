'''
반지

입력
입력은 총 2 + N 줄 이다.
첫 번째 줄에는 1 자 이상 10 자 이하의 대문자로 구성된 찾고자 하는 문자열이 적혀있다.
두 번째 줄에는 반지의 개수 N (1 ≦ N ≦ 100)이 적혀있다.
2+i 줄(1 ≦ i ≦ N)엔 i개의 반지에 새겨져있고, 10 문자로 이루어진 문자열이 적혀있다.

출력
찾고자하는 문자열을 포함 반지의 개수를 나타내는 정수를 한 줄로 출력하라.
'''

'''
- 반지의 문자열이 10자이고 찾고자 하는 문자열이 최대 10자이므로,
같은 반지 문자열을 2개 반복한 것에 찾고자 하는 문자열이 있는지만 판단하면 된다.
* Pass/1st/00:03:17  
'''
target = input()
N = int(input())
answer = 0

for i in range(N):
    ring = input()
    if target in ring * 2:
        answer += 1
        
print(answer)