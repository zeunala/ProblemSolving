/*
활자

입력
첫째 줄에 N(1 ≤ N ≤ 2,000,000,000)이 주어진다.

출력
첫째 줄에 필요한 활자의 수를 1234567로 나눈 나머지를 출력한다.

- 자릿수를 하나씩 늘려가며 활자의 수를 계산한다.
* Pass/1st/00:07:03
*/
import java.util.*;

public class S3_1951 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long N = sc.nextLong();

        long answer = 0;
        long idx = 1;
        long idxPow = 1;

        while (idxPow <= N) {
            answer += (Math.min(idxPow * 10 - 1, N) - idxPow + 1) * idx;

            idx += 1;
            idxPow *= 10;
        }
        System.out.println(answer % 1234567);

        sc.close();
    }
}
