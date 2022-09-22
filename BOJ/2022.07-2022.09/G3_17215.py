'''
볼링 점수 계산

입력
첫째 줄에 각 기회마다 소현이가 쓰러뜨린 볼링핀의 개수가 공백없이 주어진다.
이때 스트라이크는 S, 스페어는 P, 핀을 하나도 못 쓰러뜨린 것은 -으로 주어진다.

출력
첫째 줄에 소현이의 점수를 출력한다.
'''

'''
- 문제 요구사항을 그대로 구현하면 되는 문제로 보인다.
* Fail/1st/00:26:18
'''
inputSentence = input().replace("-", "0") # S, P, 숫자만 남기기 위해, 입력에서 -을 0으로 변경함

arr1st = [0] * 12 # 첫번째에 쓰러뜨린 핀들의 개수
arr2nd = [0] * 12 # 두번째에 쓰러뜨린 핀들의 개수
totalScore = 0

tryCount = 0
idx = 0

# 우선 각 프레임에 대해 첫번째/두번째 쓰러뜨린 핀들의 개수를 각각 구한다.
while idx < len(inputSentence):
    if tryCount > 9: # 추가 프레임의 경우
        if inputSentence[idx] == 'S':
            arr1st[tryCount] = 10
        else:
            arr1st[tryCount] = int(inputSentence[idx])
        idx += 1
    else: # 일반 프레임의 경우
        if inputSentence[idx] == 'S':
            arr1st[tryCount] = 10
            idx += 1
        else:
            arr1st[tryCount] = int(inputSentence[idx])
            idx += 1
            
            if inputSentence[idx] == 'P':
                arr2nd[tryCount] = 10 - arr1st[tryCount]
            else:
                arr2nd[tryCount] = int(inputSentence[idx])
            idx += 1
    
    tryCount += 1

# 추가 점수를 계산한다.
for i in range(10):
    totalScore += (arr1st[i] + arr2nd[i])
    
    if arr1st[i] == 10: # 스트라이크인 경우 추가점수 2회
        # 1회
        totalScore += arr1st[i + 1]
        
        # 2회(1회때 스트라이크가 날 경우 남은 핀을 굴리는게 아니라 새로운 핀들 상태에서 굴리므로 이에 대한 처리)
        if arr1st[i + 1] == 10:
            totalScore += arr1st[i + 2]
        else:
            totalScore += arr2nd[i + 1]
    elif arr1st[i] + arr2nd[i] == 10: # 스페어인 경우 추가점수 1회
        totalScore += arr1st[i + 1]
        
print(totalScore)