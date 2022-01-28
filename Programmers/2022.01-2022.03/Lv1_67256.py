'''
키패드 누르기

- 문제 그대로를 구현하면 되는 문제이다.
각 경우마다 손가락 위치를 저장해놓고 2 5 8 0 입력시 참고하자.
* Pass/1st/00:11:59
'''
def distance(handPos, numberPos): # 손가락과 버튼 사이의 거리를 구함
    return abs(handPos[0]-numberPos[0]) + abs(handPos[1]-numberPos[1])

def solution(numbers, hand):
    answer = ''
    leftHand = (0, 0) # 가로방향 0, 세로방향 0에서 시작
    rightHand = (2, 0) # 가로방향 2, 세로방향 0에서 시작
    
    # 예를 들어 numberToPos[5]는 5번 버튼의 좌표를 나타낸다.
    numberToPos = [(1, 0), (0, 3), (1, 3), (2, 3), (0, 2), (1, 2), (2, 2), (0, 1), (1, 1), (2, 1)]
    
    for e in numbers:
        if e in [1, 4, 7]:
            answer += "L"
                
        elif e in [3, 6, 9]:
            answer += "R"
            
        elif e in [2, 5, 8, 0]:
            leftDistance = distance(leftHand, numberToPos[e])
            rightDistance = distance(rightHand, numberToPos[e])
            
            if leftDistance < rightDistance:
                answer += "L"
            elif leftDistance > rightDistance:
                answer += "R"
            else:
                if hand == "left":
                    answer += "L"
                elif hand == "right":
                    answer += "R"
                    
        # 손의 위치를 옮김
        if answer[-1] == "L":
            leftHand = numberToPos[e]
        elif answer[-1] == "R":
            rightHand = numberToPos[e]
        
    return answer