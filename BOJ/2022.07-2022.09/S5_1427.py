'''
소트인사이드

입력
첫째 줄에 정렬하려고 하는 수 N이 주어진다.
N은 1,000,000,000보다 작거나 같은 자연수이다.

출력
첫째 줄에 자리수를 내림차순으로 정렬한 수를 출력한다.
'''

'''
- sort함수를 이용하여 쉽게 계산할 수 있다.
* Pass/1st/00:03:43
'''
N = int(input())
arr = []

while N > 0:
    arr.append(N % 10)
    N //= 10
    
arr.sort(reverse = True)

result = ""
for e in arr:
    result += str(e)
    
print(result)