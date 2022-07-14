/*
빙고

입력
첫째 줄부터 다섯째 줄까지 빙고판에 쓰여진 수가 가장 위 가로줄부터 차례대로 한 줄에 다섯 개씩 빈 칸을 사이에 두고 주어진다.
여섯째 줄부터 열째 줄까지 사회자가 부르는 수가 차례대로 한 줄에 다섯 개씩 빈 칸을 사이에 두고 주어진다.
빙고판에 쓰여진 수와 사회자가 부르는 수는 각각 1부터 25까지의 수가 한 번씩 사용된다.

출력
첫째 줄에 사회자가 몇 번째 수를 부른 후 철수가 "빙고"를 외치게 되는지 출력한다.

- 문제 조건을 그대로 구현하면 되는 문제로 보인다.
* Pass/1st/00:14:08
*/
import java.util.*;

public class S4_2578 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Integer[] bingoField = new Integer[25]; // 빙고판 상태, 불린 숫자를 null로 바꿀 것이라 Integer로 설정
        int[] directorArr = new int[25]; // 사회자가 부를 숫자들

        for (int i = 0; i < 25; i++)
            bingoField[i] = sc.nextInt();

        for (int i = 0; i < 25; i++)
            directorArr[i] = sc.nextInt();

        for (int i = 0; i < 25; i++) {
            // 사회자가 숫자를 부름
            int nextNum = directorArr[i];

            // 부른 숫자를 지움
            for (int j = 0; j < 25; j++)
                if (bingoField[j] != null && bingoField[j] == nextNum)
                    bingoField[j] = null;

            // 빙고 줄 수가 3줄 이상인지 체크
            int bingoLine = 0;
            for (int j = 0; j < 5; j++) {
                // 가로 줄 체크
                if (bingoField[5 * j] == null
                    && bingoField[5 * j + 1] == null
                    && bingoField[5 * j + 2] == null
                    && bingoField[5 * j + 3] == null
                    && bingoField[5 * j + 4] == null)
                    bingoLine++;
                
                // 세로 줄 체크
                if (bingoField[j] == null
                    && bingoField[j + 5] == null
                    && bingoField[j + 10] == null
                    && bingoField[j + 15] == null
                    && bingoField[j + 20] == null)
                    bingoLine++;
            }
            // 대각선 줄 체크
            if (bingoField[0] == null
                && bingoField[6] == null
                && bingoField[12] == null
                && bingoField[18] == null
                && bingoField[24] == null)
                bingoLine++;

            if (bingoField[4] == null
                && bingoField[8] == null
                && bingoField[12] == null
                && bingoField[16] == null
                && bingoField[20] == null)
                bingoLine++;
            
            if (bingoLine >= 3) {
                System.out.println(i + 1);
                break;
            }
        }

        sc.close();
    }
}
