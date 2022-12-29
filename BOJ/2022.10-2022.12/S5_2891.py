'''
카약과 강풍

입력
첫째 줄에 팀의 수 N, 카약이 손상된 팀의 수 S, 카약을 하나 더 가져온 팀의 수 R이 주어진다. (2 ≤ N ≤ 10, 1 ≤ S, R ≤ N)
둘째 줄에는 카약이 손상된 팀의 번호가 주어진다. 팀 번호는 중복되지 않는다.
셋째 줄에는 카약을 하나 더 가져온 팀의 번호가 주어진다. 팀 번호는 중복되지 않는다.
출력
첫째 줄에 출발을 할 수 없는 팀의 최솟값을 출력한다.
'''

'''
- 여분 카약을 앞뒤로 밖에 빌려줄 수 없으므로 그리디 알고리즘으로 접근한다.
우선 손상+여분 있는 팀을 제외하고, 손상된 팀/여분 팀으로 나누어 각각을 오름차순으로 정렬한 후 손상된 팀 앞번부터 찾는다.
* Fail/1st/00:14:34
- 두 배열에서 중복되는 걸 빼는 과정에서 breakArr에서 중복 제외한 이후의 배열을 기준으로 oneMoreArr을 수정한게 문제로 보여 수정하였다.
* Pass/2nd/00:17:20
'''
N, S, R = map(int, input().split()) # N: 팀의 수, S: 손상 팀의 수, R: 여분 팀의 수
breakArrTemp = list(map(int, input().split()))
oneMoreArrTemp = list(map(int, input().split()))
    
breakArr = [e for e in breakArrTemp if e not in oneMoreArrTemp] # 여분 팀의 수와 중복된 걸 뺌
oneMoreArr = [e for e in oneMoreArrTemp if e not in breakArrTemp] # 손상 팀의 수와 중복된 걸 뺌
breakArr.sort()
oneMoreArr.sort()

answer = 0
breakArrIdx = 0
oneMoreArrIdx = 0

while breakArrIdx < len(breakArr) and oneMoreArrIdx < len(oneMoreArr):
    if abs(breakArr[breakArrIdx] - oneMoreArr[oneMoreArrIdx]) <= 1: # 빌려줄 수 있는 상황
        breakArrIdx += 1
        oneMoreArrIdx += 1
    elif breakArr[breakArrIdx] + 1 < oneMoreArr[oneMoreArrIdx]:
        # 너무 앞에 있어서 현재 남은 여분 팀의 수 가장 앞 번으로도 못 빌려주는 경우
        breakArrIdx += 1
        answer += 1
    elif breakArr[breakArrIdx] > oneMoreArr[oneMoreArrIdx] + 1: 
        # 뒤에 있어서 현재 남은 여분 가장 앞 번으로는 못빌려주므로 다음 여분 확인
        oneMoreArrIdx += 1

answer += len(breakArr) - breakArrIdx # 여분 팀이 더 이상 없음

print(answer)