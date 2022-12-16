/*
매직스퀘어

입력
첫째 줄에 N(3 ≤  N ≤ 100)가 주어지고 둘째 줄부터 N개의 줄에 걸쳐 N개의 숫자가 주어진다.
N개의 수의 범위는 1이상 n2이하 이다.

출력
입력된 N개의 숫자가 나타내는 정방행렬이 매직스퀘어라면 TRUE, 아니라면 FALSE를 출력한다.

- N의 범위가 작으므로 문제의 요구사항을 그대로 구현하면 되는 문제이다.
* Fail/1st/00:09:05
- 1부터 n*n까지로 중복없이 모든 수가 달라야 한다는 조건을 추가로 체크하도록 수정하였다.
* Pass/2nd/00:13:23
*/
import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

public class S5_15739 {
    public static boolean isMagicSquare(int[][] arr, int N) {
        int sumOfLine = N * (N * N + 1) / 2; // 각 가로, 세로, 대각선 수열의 합
        Set<Integer> allNumber = new HashSet<>(); // 모든 숫자들

        // 1~n*n까지 중복이 아닌지 체크
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (arr[i][j] < 1 || arr[i][j] > N * N) {
                    return false;
                }
                allNumber.add(arr[i][j]);
            }
        }
        if (allNumber.size() != N * N) {
            return false;
        }

        // 가로, 세로 체크
        for (int i = 0; i < N; i++) {
            int temp1 = 0;
            int temp2 = 0;
            for (int j = 0; j < N; j++) {
                temp1 += arr[i][j];
                temp2 += arr[j][i];
            }
            if (temp1 != sumOfLine || temp2 != sumOfLine) {
                return false;
            }
        }

        // 대각선 체크
        int cross1 = 0;
        int cross2 = 0;
        for (int i = 0; i < N; i++) {
            cross1 += arr[i][N - 1 - i];
            cross2 += arr[N - 1 - i][i];
        }
        if (cross1 != sumOfLine || cross2 != sumOfLine) {
            return false;
        }

        return true;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[][] arr = new int[N][N];
        
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                arr[i][j] = sc.nextInt();
            }
        }

        if (isMagicSquare(arr, N)) {
            System.out.println("TRUE");
        } else {
            System.out.println("FALSE");
        }

        sc.close();
    }
}
