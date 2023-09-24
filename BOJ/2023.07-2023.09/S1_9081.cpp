/*
단어 맞추기

입력
입력의 첫 줄에는 테스트 케이스의 개수 T (1 ≤ T ≤ 10)가 주어진다.
각 테스트 케이스는 하나의 단어가 한 줄로 주어진다.
단어는 알파벳 A~Z 대문자로만 이루어지며 항상 공백이 없는 연속된 알파벳으로 이루어진다.
단어의 길이는 100을 넘지 않는다.

출력
각 테스트 케이스에 대해서 주어진 단어 바로 다음에 나타나는 단어를 한 줄에 하나씩 출력하시오.
만일 주어진 단어가 마지막 단어이라면 그냥 주어진 단어를 출력한다.

- C++의 next_permutation으로 쉽게 구할 수 있다.
* Pass/1st/00:08:20
*/
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(void) {
    int T;

    cin >> T;

    for (int testCase = 0; testCase < T; testCase++) {
        string inputText;

        cin >> inputText;

        vector<char> text;
        for (int i = 0; i < inputText.size(); i++) {
            text.push_back(inputText[i]);
        }

        bool hasNext = next_permutation(text.begin(), text.end());
        if (!hasNext) {
            prev_permutation(text.begin(), text.end());
        }
        for (char e : text) {
            cout << e;
        }
        cout << endl;
    }
}