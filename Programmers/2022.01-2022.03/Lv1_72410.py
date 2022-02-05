'''
신규 아이디 추천

- 문제 조건 그대로 구현만 하면 되는 문제로 보인다.
* Pass/1st/00:10:39
'''

def solution(new_id):
    # 1단계
    step1 = new_id.lower()
    
    # 2단계
    step2 = ""
    for e in step1:
        if e in "abcdefghijklmnopqrstuvwxyz0123456789-_.":
            step2 += e
    
    # 3단계
    step3 = ""
    lastChar = ""
    for e in step2:
        if e == "." and lastChar == ".": # 연속 .는 패스
            continue
        else:
            lastChar = e
            step3 += e
    
    # 4단계
    step4 = ""
    if step3[0] == ".":
        step4 = step3[1:-1]
    else:
        step4 = step3[0:-1]
    if step3[-1] != ".":
        step4 += step3[-1]
        
    # 5단계
    step5 = ""
    if step4 == "":
        step5 = "a"
    else:
        step5 = step4

        
    # 6단계
    step6 = ""
    if len(step5) >= 16:
        if step5[14] == ".":
            step6 = step5[:14]
        else:
            step6 = step5[:15]
    else:
        step6 = step5
    
    # 7단계
    step7 = step6
    while len(step7) <= 2:
        step7 += step7[-1]
    
    return step7