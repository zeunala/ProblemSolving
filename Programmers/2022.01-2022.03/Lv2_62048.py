'''
멀쩡한 사각형

- 세로가 긴 형태로 만들고 각 가로 1칸마다 못쓰게 되는 칸의 수를 구해보자.
* Fail/1st/00:20:46
- 선을 그어서 못 쓰는 부분을 합치면 가로 부분 + 세로 부분과 같음을 이용하되 이 때 최대공약수만큼 중복되므로 빼주도록 하자.
* Pass/2nd/00:24:00
'''
import math

def solution(w,h):
    # 사용할 수 없는 블록
    unable = w + h - math.gcd(w, h)
    
    return w * h - unable