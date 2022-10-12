'''
삼각형 만들기

력
첫째 줄에 빨대의 개수 N이 주어진다.
N은 3보다 크거나 같고, 1,000,000보다 작거나 같은 자연수이다.
둘째 줄부터 N개의 줄에 빨대의 길이가 한 줄에 하나씩 주어진다.
빨대의 길이는 1,000,000보다 작거나 같은 자연수이다.

출력
첫째 줄에 삼각형 세 변의 길이의 합의 최댓값을 출력한다. 만약 삼각형을 만들 수 없으면 -1을 출력한다.
'''

'''
- 빨대의 길이가 100만이하인 점을 이용하여 빨대를 내림차순으로 빠르게 정렬하고 가장 큰 변 3개를 선택한다.
만약 가장 큰 변이 다른 두 변 합 이상이라 삼각형이 만들어지지 않는다면 가장 큰 변을 제외하고 반복한다.
길이가 100만 이하이므로 시간초과가 나는 예외 케이스를 걱정할 필요가 없다.
* Pass/1st/00:10:16
- 문제를 풀고 다른 사람의 풀이를 본 결과 그냥 sort()를 쓰더라도 시간초과 걱정을 할 필요는 없어보인다.
여담으로 input = sys.stdin.readline 로 빠르게 입력받는 편법이 있음도 알게 되었다.
'''
import sys

N = int(sys.stdin.readline().rstrip())
arr = [0] * 1000001 # arr[i]는 빨대의 길이가 i인게 몇 개 있는지

for i in range(N):
    temp = int(sys.stdin.readline().rstrip())
    arr[temp] += 1
    
sortedArr = [] # arr배열을 내림차순으로 정렬
for i in range(len(arr) - 1, 0 , -1):
    while arr[i] > 0:
        sortedArr.append(i)
        arr[i] -= 1
        
result = -1
for i in range(len(sortedArr) - 2):
    a, b, c = sortedArr[i], sortedArr[i + 1], sortedArr[i + 2] # 삼각형 크기 큰 것 3개 선택
    if a < b + c: # 삼각형이 만들어질 경우
        result = a + b + c
        break
    
print(result)