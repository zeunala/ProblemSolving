'''
팩토리얼5

입력
첫째 줄에 정수 N이 주어진다. N은 1,000,000보다 작거나 같다.
또, 9보다 크거나 같다.

출력
첫째 줄에 N의 팩토리얼5를 계산한다.
'''

'''
- 매 반복마다 맨 뒤 0들을 제거하는 식으로 진행한다.
* Fail/1st/00:32:10
'''

N = int(input())
result = 1


for i in range(2, N+1):
    result *= i
    
    while result % 10 == 0 and result > 0:
        result //= 10
        
    result %= 100000
    
print(str(result)[-5:])