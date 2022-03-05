'''
LCS

입력
첫째 줄과 둘째 줄에 두 문자열이 주어진다.
문자열은 알파벳 대문자로만 이루어져 있으며, 최대 1000글자로 이루어져 있다.

출력
첫째 줄에 입력으로 주어진 두 문자열의 LCS의 길이를 출력한다.
'''

'''
- 2차원 배열을 만들어서 각 문자열의 최장 공통 부분 수열의 길이를 저장하도록 한다.
* Pass/1st/00:12:21
'''
stringA = input()
stringB = input()

# dp[a][b]는 stringA[:a+1]과 stringB[:b+1]의 LCS
dp = [[0 for _ in range(len(stringA) + 1)] for _ in range(len(stringB) + 1)]
        
for i in range(1, len(stringB) + 1):
    for j in range(1, len(stringA) + 1):
        if stringB[i-1] == stringA[j-1]:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j], dp[i-1][j-1] + 1)
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])
            
print(dp[-1][-1])