/*
제로

입력
첫 번째 줄에 정수 K가 주어진다. (1 ≤ K ≤ 100,000)
이후 K개의 줄에 정수가 1개씩 주어진다.
정수는 0에서 1,000,000 사이의 값을 가지며, 정수가 "0" 일 경우에는 가장 최근에 쓴 수를 지우고, 아닐 경우 해당 수를 쓴다.
정수가 "0"일 경우에 지울 수 있는 수가 있음을 보장할 수 있다.

출력
재민이가 최종적으로 적어 낸 수의 합을 출력한다. 최종적으로 적어낸 수의 합은 2^31-1보다 작거나 같은 정수이다.

- 스택을 만들어 나중에 남는 수들의 합을 구하면 될 것이다.
* Pass/1st/00:08:33
*/
import java.util.Scanner;

public class S4_10773 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] arr = new int[100001];
        int arrIdx = -1; // arr의 끝 원소의 인덱스
        int answer = 0;

        int K = sc.nextInt();

        for (int i = 0; i < K; i++) {
            int num = sc.nextInt();

            if (num == 0) {
                arrIdx--;
            } else {
                arr[++arrIdx] = num;
            }
        }

        for (int i = 0; i <= arrIdx; i++)
            answer += arr[i];

        System.out.println(answer);

        sc.close();
    }
}
