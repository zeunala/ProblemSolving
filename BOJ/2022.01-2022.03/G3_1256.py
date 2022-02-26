'''
사전

입력
첫째 줄에 세 정수 N, M, K가 순서대로 주어진다.

출력
첫째 줄에 규완이의 사전에서 K번째 문자열을 출력한다.
만약 규완이의 사전에 수록되어 있는 문자열의 개수가 K보다 작으면 -1을 출력한다.
'''

'''
- 예를 들어 a가 3개, z가 2개 있다면 aaazz, aazaz, aazza, azaaz, azaza, azzaa, ... 순이며,
총 경우의 수는 5C3이고, a가 맨 앞부터 시작했을 때 a의 위치를 고르는 조합의 개수이다.
총 경우의 수 (n+m)Cm중 맨 앞에 a가 오는 경우의 수는 (n-1+m)Cm이므로 이를 이용해 가지치기 한다.
* Pass/1st/00:28:10
'''
def factCal(m): # m!값 리턴
    value = 1
    
    for i in range(1, m + 1):
        value *= i
        
    return value

def combinationCal(m, n): # mCn의 값 리턴
    return factCal(m)//(factCal(m-n)*factCal(n))

N, M, K = map(int, input().split())

if combinationCal((N+M), N) < K:
    print(-1)
else:
    # N: 남은 a의 수, M: 남은 z의 수, K: 남은 인덱스
    result = ""
    
    while N > 0: # a가 나올만큼 다 나올 때까지 체크
        if M == 0: # z가 나올만큼 다 나왔으면 뒤에 a만 붙여줌
            result += "a"
            N -= 1
            continue
        
        # 만약 현재 result에 이어서 a가 오는 모든 경우의 수 < 현재 K라면, 현재 result에 z가 와야 할 것이다.
        if combinationCal(((N-1)+M), M) < K:
            K -= combinationCal(((N-1)+M), M)
            result += "z"
            M -= 1
        else:
            result += "a"
            N -= 1
            
    while M > 0: # 남은 z를 붙여줌
        M -= 1
        result += "z"
        
    print(result)