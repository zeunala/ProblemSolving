/*
너의 티어는?

입력
입력의 첫째 줄에 게임에서 승리할 확률 W, 질 확률 L,비길 확률 D가 0 이상의 실수로 주어진다.
(W+L+D=1) 입력은 소수점 둘째짜리까지 들어온다.

출력
브론즈, 실버, 골드, 플래티넘, 다이아에 배정받을 확률을 각 줄에 출력한다.
(소수점 아래 9번째 자리에서 반올림하여 소수점 8자리까지 출력)

- 20경기를 진행하므로 승수-패수는 -20부터 +20까지 가능하다.
경기를 1번째부터 마지막까지 진행하며 확률을 갱신해나간다.
* Pass/1st/00:29:59
- 문제 풀이 이후 다른 자료를 찾아보니 String.format(...)을 사용하여 좀 더 쉽게 나타낼 수 있을 것으로 보인다.
*/
import java.util.*;
import java.math.*;

public class S1_14613 {
    private static final int MID_IDX = 20;

    private static int scoreToIdx(int score) {
        return score + MID_IDX;
    }

    private static void printScoreAToB(double[] arr, int a, int b) {
        double result = 0;
        for (int i = scoreToIdx(a); i <= scoreToIdx(b); i++) {
            result += arr[i];
        }
        System.out.printf("%.8f\n", Math.round(result * 100000000) / (double) 100000000);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        double W = sc.nextDouble();
        double L = sc.nextDouble();
        double D = sc.nextDouble();

        double[] currentProbability = new double[41]; // 승점이 -20가 될 확률 ~ +20이 될 확률이 차례로 담긴다.

        Arrays.fill(currentProbability, 0);
        currentProbability[MID_IDX] = 1;

        for (int round = 0; round < 20; round++) {
            double[] nextProbability = new double[41];
            Arrays.fill(nextProbability, 0);

            for (int i = 0; i < nextProbability.length; i++) {
                if (i - 1 >= 0) {
                    nextProbability[i] += currentProbability[i - 1] * W;
                }
                nextProbability[i] += currentProbability[i] * D;
                if (i + 1 < nextProbability.length) {
                    nextProbability[i] += currentProbability[i + 1] * L;
                }
            }

            currentProbability = nextProbability;
        }
        
        // 브론즈: 승점 -20 ~ -11
        printScoreAToB(currentProbability, -20, -11);
        // 실버: 승점 -10 ~ -1
        printScoreAToB(currentProbability, -10, -1);
        // 골드: 승점 0 ~ 9
        printScoreAToB(currentProbability, 0, 9);
        // 플래티넘: 승점 10 ~ 19
        printScoreAToB(currentProbability, 10, 19);
        // 다이아: 승점 20
        printScoreAToB(currentProbability, 20, 20);

        sc.close();
    }
}
