'''
평행사변형

입력
첫째 줄에 xA yA xB yB xC yC가 주어진다.
모두 절댓값이 5000보다 작거나 같은 정수이다.

출력
첫째 줄에 문제의 정답을 출력한다. 절대/상대 오차는 10^-9까지 허용한다.
'''

'''
- 세 점이 한 줄 위에 있으면 평행사변형을 만들 수 없다.
세 점을 이은 세 변의 길이 중 ((가장긴 두변) - (가장짧은 두변)) * 2를 출력한다.
* Pass/1st/00:11:05
'''
import math

Xa, Ya, Xb, Yb, Xc, Yc = map(int, input().split())

if (Yb - Ya) * (Xc - Xb) == (Yc - Yb) * (Xb - Xa): # 세 점이 한 줄 위에 있는 경우
    print(-1.0)
else:
    threeSlide = []
    threeSlide.append(math.sqrt((Xb - Xa)**2 + (Yb - Ya)**2))
    threeSlide.append(math.sqrt((Xc - Xa)**2 + (Yc - Ya)**2))
    threeSlide.append(math.sqrt((Xc - Xb)**2 + (Yc - Yb)**2))
    
    threeSlide.sort()
    print(((threeSlide[1] + threeSlide[2]) - (threeSlide[0] + threeSlide[1])) * 2)