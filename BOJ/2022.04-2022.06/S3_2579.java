/*
계단 오르기

입력
입력의 첫째 줄에 계단의 개수가 주어진다.
둘째 줄부터 한 줄에 하나씩 제일 아래에 놓인 계단부터 순서대로 각 계단에 쓰여 있는 점수가 주어진다.
계단의 개수는 300이하의 자연수이고, 계단에 쓰여 있는 점수는 10,000이하의 자연수이다.

출력
첫째 줄에 계단 오르기 게임에서 얻을 수 있는 총 점수의 최댓값을 출력한다.

- 1칸/2칸, 2칸 세 가지 경우의 수 중 점수가 최대인 경우를 고르면 된다.
* Fail/1st/00:17:25
*/
import java.lang.*;
import java.util.*;

public class S3_2579 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt(); // 계단 개수
        int[] arr = new int[N + 1]; // arr[i]는 i번째 계단의 점수
        int[] dp = new int[N + 1]; // dp[i]는 i번째 계단에서 시작했을 때 얻을 수 있는 최대 점수

        arr[0] = 0;
        for (int i = 1; i <= N; i++)
            arr[i] = sc.nextInt();

        for (int i = N; i >= 0 ; i--) {
            if (i == N) { // 바로 끝 지점인 경우 해당 칸의 점수 먹고 종료
                dp[i] = arr[i];
            } else if (i == N - 1) { // 끝 1칸 전인 경우 현재 칸과 다음 칸의 점수 먹고 종료
                dp[i] = arr[i] + arr[i + 1];
            } else if (i == N - 2) { // 끝 2칸 전의 경우 현재 칸 + 다음 칸 + 다다음칸 점수 먹고 종료(모든 점수는 양수이므로)
                dp[i] = arr[i] + arr[i + 1] + arr[i + 2];
            } else if (i == N - 3) { // 끝 3칸 전의 경우 1칸 + 2칸 가는 경우와 2칸 + 1칸 가는 경우 중 최댓값
                dp[i] = arr[i] + Math.max(arr[i + 1] + arr[i + 3], arr[i + 2] + arr[i + 3]);
            } else { // 그 외에는 1칸/2칸, 2칸 중 최댓값 선택
                dp[i] = arr[i] + Math.max(arr[i + 1] + dp[i + 3], dp[i + 2]);
            }
        }
        System.out.println(dp[0]);
        
        sc.close();
    }
}
