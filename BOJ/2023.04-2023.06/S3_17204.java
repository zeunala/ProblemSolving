/*
죽음의 게임

입력
첫 번째 줄에 게임에 참여하는 사람의 수 N(3 ≤ N ≤ 150)과 보성이의 번호 K(1 ≤ K ≤ N - 1)가 공백을 두고 주어진다.
두번째 줄부터 N줄에 걸쳐 i(0 ≤ i ≤ N - 1)번 사람이 지목하는 사람의 번호 ai(0 ≤ ai ≤ N - 1)가 주어진다.
자기 자신을 지목하는 경우도 존재할 수 있다.

출력
영기가 말해야 하는 가장 작은 양의 정수 M을 출력한다. 만약 어떤 방법으로도 보성이가 걸리지 않는다면 -1을 출력한다.

- N의 범위가 작으므로 문제의 요구사항을 그대로 구현한다.
* Pass/1st/00:09:46
*/
import java.util.*;

public class S3_17204 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int K = sc.nextInt();
        int[] arr = new int[N]; // arr[i]는 i번 사람이 지목한 번호

        for (int i = 0; i < N; i++) {
            arr[i] = sc.nextInt();
        }

        int answer = -1;
        for (int i = 1; i <= N; i++) { // 불러야 하는 숫자 M은 N을 넘지 않는다.
            int target = arr[0];

            for (int j = 1; j < i; j++) {
                target = arr[target];
            }

            if (target == K) {
                answer = i;
                break;
            }
        }

        System.out.println(answer);
    }
}
