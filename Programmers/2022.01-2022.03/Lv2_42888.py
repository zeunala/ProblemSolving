'''
오픈 채팅방

- 우선 마지막 시점을 기준으로 닉네임을 전부 다 변환한 이후,
처음부터 Enter와 Leave에 대한 메시지를 찍어내면 된다.
* Pass/1st/00:12:07
'''

def solution(record):
    answer = []
    
    uidToNickname = {} # uid와 닉네임을 매칭시키기 위해 딕셔너리 사용
    
    # 딕셔너리를 갱신한다.
    for e in record:
        message = e.split()[0]
        uid = e.split()[1]
        if message == "Enter" or message == "Change":
            nickname = e.split()[2]
        
        # 새로 들어온 사람들을 딕셔너리에 추가 / 닉네임을 바꾼 경우 딕셔너리 내용 수정
        if message == "Enter" or message == "Change":
            uidToNickname[uid] = nickname
    
    # 메시지를 만든다.
    for e in record:
        message = e.split()[0]
        uid = e.split()[1]
        nickname = uidToNickname[uid]
        
        if message == "Enter":
            answer.append(nickname + "님이 들어왔습니다.")
        if message == "Leave":
            answer.append(nickname + "님이 나갔습니다.")
        
    return answer