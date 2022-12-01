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
- 끝 2칸 전에서의 조건을 수정하였다.
* Fail/2nd/00:20:18
- 5 100 100 100 100 1 의 경우 1, 2, 4, 5번째 칸을 밟아 301까지 가능하지만 201이 나오는 반례가 있다.
시작점은 계단에 포함되지 않기에 arr[0] -> arr[1] -> arr[2]가 가능한데 이를 놓친 것으로 보인다.
또한 else if (i == N - 3) 부분은 불필요하므로 삭제해도 될 것이다.
* Fail/3rd/00:39:20
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
            } else if (i == N - 2) { // 끝 2칸 전의 경우 현재 칸 + 다다음칸 점수 먹고 종료
                if (i == 0) { // 시작점인 경우 연달아 세 칸을 건널 수도 있다.
                    dp[i] = arr[i] + arr[i + 1] + arr[i + 2];
                } else {
                    dp[i] = arr[i] + arr[i + 2];
                }
            } else { // 그 외에는 1칸/2칸, 2칸 중 최댓값 선택
                if (i == 0) { // 시작점인 경우 1칸/1칸, 1칸/2칸이 가능하다. (계단점수가 자연수이므로 2칸보다 1칸/1칸이 무조건 유리)
                    dp[i] = arr[i] + Math.max(arr[i + 1] + dp[i + 3], arr[i + 1] + dp[i + 2]);
                } else {
                    dp[i] = arr[i] + Math.max(arr[i + 1] + dp[i + 3], dp[i + 2]);
                }
            }
        }
        System.out.println(dp[0]);
        
        sc.close();
    }
}
