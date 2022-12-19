'''
랜선 자르기

입력
첫째 줄에는 오영식이 이미 가지고 있는 랜선의 개수 K, 그리고 필요한 랜선의 개수 N이 입력된다.
K는 1이상 10,000이하의 정수이고, N은 1이상 1,000,000이하의 정수이다. 그리고 항상 K ≦ N 이다.
그 후 K줄에 걸쳐 이미 가지고 있는 각 랜선의 길이가 센티미터 단위의 정수로 입력된다.
랜선의 길이는 2^31-1보다 작거나 같은 자연수이다.

출력
첫째 줄에 N개를 만들 수 있는 랜선의 최대 길이를 센티미터 단위의 정수로 출력한다.
'''

'''
- 만들 수 있는 랜선의 길이들은 연속적이고 최댓값이 존재하므로, 파라매트릭 서치를 이용한다.
* Pass/1st/00:08:55
'''
import sys

def isValidMake(arrN, N, length): # arrN의 랜선을 length길이만큼 N개이상 만들 수 있는지 반환
    if length == 0:
        return True
    
    result = 0
    for e in arrN:
        result += e // length
    return result >= N

K, N = map(int, sys.stdin.readline().rstrip().split()) # K: 랜선 개수, N: 필요 랜선 개수
arrN = [] # arr[i]는 i번째 랜선의 길이 (i>=0)

for i in range(K):
    arrN.append(int(sys.stdin.readline().rstrip()))
    
minLength = 0
maxLength = 2 ** 31
maxAnswer = 0

while minLength <= maxLength:
    midLength = (minLength + maxLength) // 2
    if isValidMake(arrN, N, midLength):
        if maxAnswer < midLength:
            maxAnswer = midLength
        minLength = midLength + 1
    else:
        maxLength = midLength - 1
        
print(maxAnswer)