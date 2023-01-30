'''
문자열 잘라내기

입력
첫 번째 줄에는 테이블의 행의 개수와 열의 개수인 R과 C가 주어진다. (2 ≤ R, C ≤ 1000)
이후 R줄에 걸쳐서 C개의 알파벳 소문자가 주어진다.
가장 처음에 주어지는 테이블에는 열을 읽어서 문자열을 만들 때, 동일한 문자열이 존재하지 않는 입력만 주어진다.

출력
문제의 설명과 같이 count의 값을 출력한다.
'''

'''
- R과 C의 범위가 크지 않으므로 문제의 요구사항을 그대로 구현하면 된다.
한 줄씩 지우면서 동일한 문자열이 존재할 때까지 반복한다.
* Pass/1st/00:12:59
'''
R, C = map(int, input().split())
arr = [""] * C # arr[i]는 i열에 있는 것만 모은 문자열

for i in range(R):
    inputSentence = input()
    for j in range(len(inputSentence)):
        arr[j] = arr[j] + inputSentence[j]

tempSet = set(arr)
count = 0

while True:
    newSet = set() # 맨 앞의 글자(즉 맨 위의 행)를 지운 새로운 문자열들만 모은 것
    isDuplicated = False
    
    for e in tempSet:
        newE = e[1:] # 맨 앞의 글자(즉 맨 위의 행)를 지운 새로운 문자열
        if newE in newSet:
            isDuplicated = True
            break
        newSet.add(newE)
        
    if isDuplicated: # 중복된 문자열이 있다면 count 늘리지 않고 바로 종료
        break
    
    count += 1
    tempSet = newSet

print(count)