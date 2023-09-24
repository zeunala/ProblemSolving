/*
틱택토

입력
입력은 여러 개의 테스트 케이스로 이루어져 있다.
각 줄은 9개의 문자를 포함하며, 'X', 'O', '.' 중 하나이다.
'.'은 빈칸을 의미하며, 9개의 문자는 게임판에서 제일 윗 줄 왼쪽부터의 순서이다. 입력의 마지막에는 문자열 "end"가 주어진다.

출력
각 테스트 케이스마다 한 줄에 정답을 출력한다. 가능할 경우 "valid", 불가능할 경우 "invalid"를 출력한다.

- 1번째 조건으로 O또는 X가 승리하거나, 게임판이 가득 차야한다.
2번째 조건으로 O가 승리하면 O와 X의 수가 같아야 하고, X가 승리하거나 무승부이면 X가 O보다 1개 많아야 한다.
* Fail/1st/00:38:19
- O또는 X가 동시에 승리하면 안된다는 조건을 추가하였다.
* Fail/2nd/00:41:18
- 빠진 코드를 수정하였다.
* Fail/3rd/00:42:24
*/
#include <iostream>
#include <string>

using namespace std;

int findWinner(string map[][3], int N = 3) { // O 승리 시 1, X 승리 시 2, 무승부 시 0, 이때 게임판이 가득 차면 -1, 유효하지 않으면 -2
    bool winO = false;
    bool winX = false;

    for (int i = 0; i < N; i++) {
        if ((map[i][0] == "O" && map[i][1] == "O" && map[i][2] == "O")
        || (map[0][i] == "O" && map[1][i] == "O" && map[2][i] == "O")) {
            winO = true;
        } else if ((map[i][0] == "X" && map[i][1] == "X" && map[i][2] == "X")
        || (map[0][i] == "X" && map[1][i] == "X" && map[2][i] == "X")) {
            winX = true;
        }
    }

    if ((map[0][0] == "O" && map[1][1] == "O" && map[2][2] == "O")
    || (map[0][2] == "O" && map[1][1] == "O" && map[2][0] == "O")) {
        winO = true;
    } else if ((map[0][0] == "X" && map[1][1] == "X" && map[2][2] == "X")
    || (map[0][2] == "X" && map[1][1] == "X" && map[2][0] == "X")) {
        winX = true;
    }

    if (winO && winX) {
        return -2;
    }
    if (winO) {
        return 1;
    }
    if (winX) {
        return 2;
    }

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            if (map[i][j] == ".") {
                return 0;
            }
        }
    }
    return -1;
}

int countChar(string map[][3], string target, int N = 3) { // 주어진 문자가 몇 개 있는지 확인
    int result = 0;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            if (map[i][j] == target) {
                result++;
            }
        }
    }
    return result;
}

int main(void) {
    string inputLine;

    do {
        string map[3][3];
        cin >> inputLine;

        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                map[i][j] = inputLine[i * 3 + j];
            }
        }

        int winner = findWinner(map, 3);

        if (winner == 0) { // 누가 이기지도 않고 게임판이 꽉 차지도 않음
            cout << "invalid" << endl;
        } else if (winner == 1) { // O가 승리하면 O와 X의 수가 같아야 한다.
            if (countChar(map, "O") == countChar(map, "X")) {
                cout << "valid" << endl;
            } else {
                cout << "invalid" << endl;
            }
        } else if (winner == -2) { // 유효하지 않은 경우
            cout << "invalid" << endl;
        } else { // X가 승리하면 X가 O보다 1개 더 많아야 한다.
            if (countChar(map, "O") + 1 == countChar(map, "X")) {
                cout << "valid" << endl;
            } else {
                cout << "invalid" << endl;
            }
        }
        
    } while (inputLine != "end");
}