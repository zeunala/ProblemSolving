'''
멀쩡한 사각형

- 세로가 긴 형태로 만들고 각 가로 1칸마다 못쓰게 되는 칸의 수를 구해보자.
* Fail/1st/00:20:46
'''
import math

def solution(w,h):
    # h >= w인 상태로 맞추어준다.
    if w > h:
        w, h = h, w
    
    # 사용할 수 없는 블록
    unable = w * math.ceil(h / w)
    
    return w * h - unable