/*
빗물

입력
첫 번째 줄에는 2차원 세계의 세로 길이 H과 2차원 세계의 가로 길이 W가 주어진다. (1 ≤ H, W ≤ 500)
두 번째 줄에는 블록이 쌓인 높이를 의미하는 0이상 H이하의 정수가 2차원 세계의 맨 왼쪽 위치부터 차례대로 W개 주어진다.
따라서 블록 내부의 빈 공간이 생길 수 없다. 또 2차원 세계의 바닥은 항상 막혀있다고 가정하여도 좋다.

출력
2차원 세계에서는 한 칸의 용량은 1이다. 고이는 빗물의 총량을 출력하여라.
빗물이 전혀 고이지 않을 경우 0을 출력하여라.

- 1층부터 차례대로, 막혀있는 두 블록 사이에 존재하는 빈 공간의 개수를 체크한다.
예를 들어 OO..O이면 2개, O...O이면 3개, O.O..이면 1개이다.
* Fail/1st/00:25:12/RuntimeError
*/
#include <iostream>

using namespace std;

int main(void) {
    int H, W; // H: 세로, W: 가로
    int *arr = new int[W];

    cin >> H >> W;
    for (int i = 0; i < W; i++) {
        cin >> arr[i];
    }

    int answer = 0;
    for (int currentH = 0; currentH < H; currentH++) {
        bool isCount = false;
        int currentCount = 0;
        
        for (int currentW = 0; currentW < W; currentW++) {
            if (arr[currentW] >= (currentH + 1)) { // 막혀있음
                if (isCount) {
                    answer += currentCount;
                    currentCount = 0;
                    continue;
                }
                isCount = true;
            } else { // 뚫려있음
                if (isCount) {
                    currentCount++;
                }
            }
        }
    }
    cout << answer;

    delete []arr;
}