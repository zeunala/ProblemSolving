/*
수 이어가기

입력
첫 번째 수가 주어진다. 이 수는 30,000 보다 같거나 작은 양의 정수이다.
출력
첫 번째 줄에는 입력된 첫 번째 수로 시작하여 위의 규칙에 따라 만들 수 있는 수들의 최대 개수를 출력한다.
둘째 줄에 그 최대 개수의 수들을 차례대로 출력한다. 이들 수 사이에는 빈칸을 하나씩 둔다.

- 수의 범위가 작으므로 1부터 해당 수까지를 하나하나 체크해본다.
* Fail/1st/00:15:08
*/

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class S5_2635 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        Integer N = Integer.parseInt(br.readLine());

        int answer = 0; // 최대 개수
        List<Integer> answerArr = new ArrayList<>(); // 그 때의 수들

        for (int i = 1; i <= N; i++) {
            List<Integer> tempArr = new ArrayList<>();
            int nextNum = N - i;

            tempArr.add(N);
            while (nextNum >= 0) {
                tempArr.add(nextNum);
                nextNum = tempArr.get(tempArr.size() - 2) - tempArr.get(tempArr.size() - 1);
            }

            if (answer < tempArr.size()) {
                answer = tempArr.size();
                answerArr = tempArr;
            }
        }

        for (Integer e : answerArr) {
            sb.append(e);
            sb.append(" ");
        }

        System.out.println(answer);
        System.out.println(sb.toString().trim());

        br.close();
    }
}
