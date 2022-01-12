'''
문자열 압축

- s의 길이가 작으므로 문제 그대로 구현해 나가면 될 것으로 보인다.
* Fail/1st/00:22:40
- while문 종료 조건 부분을 수정하였다.
* Fail/2nd/00:28:49
- 문자열 크기가 1일 때를 생각하지 않아 틀린 것으로 보이며, answer 초기값을 len(s)로 수정하였다.
* Pass/3rd/00:32:17
'''

def solution(s):
    answer = len(s)
    
    for i in range(1, len(s)//2 + 1): # i는 몇 개 단위로 자를지를 나타낸다.
        result = "" # s를 압축한 후의 문자열
        combo = 1 # 현재 문자열이 몇 번 반복되는지
        idx = 0
        while idx + i <= len(s):
            if s[idx:idx+i] == s[idx+i:idx+2*i]:
                combo += 1
            else:
                if combo == 1:
                    result += s[idx:idx+i]
                else:
                    result += str(combo) + s[idx:idx+i]
                combo = 1
            idx += i
        # 남은 문자열 추가
        if combo == 1:
            result += s[idx:]
        else:
            result += str(combo) + s[idx:idx+i]
        
        if len(result) < answer:
            answer = len(result)
                
    return answer