/*
악수

입력
첫째 줄에 회의에 참석한 사람의 수 n (1 ≤ n ≤ 10,000,000)이 주어진다.

출력
첫째 줄에 악수를 하는 방법의 수를 출력한다. 수가 매우 커질 수 있기 때문에, 마지막 자리만 출력한다.

- 분할 정복 알고리즘으로 풀면 될 것으로 보인다.
2n명 -> n명과 n명으로 쪼갠 후 각 경우의 수의 곱 + 나눈 경계에서 악수하는 경우의 수까지 고려(n-1명과 n-1명)
2n+1명 -> 마찬가지로 n+1명과 n명으로 쪼개서 계산
* Pass/1st/00:14:35
*/
import java.util.*;

public class S3_8394 {
    public static Map<Integer, Integer> dp = new HashMap<>(); // dp.get(n)은 n명이 악수하는 경우의 수의 일의 자리값

    public static int calc(int n) {
        int result;

        if (dp.get(n) != null)
            return dp.get(n);
        
        if (n % 2 == 0) { // 2n명 -> n명과 n명으로 쪼갠 후 각 경우의 수의 곱 + 나눈 경계에서 악수하는 경우의 수까지 고려(n-1명과 n-1명)
            result = (calc(n / 2) * calc(n / 2) + calc(n / 2 - 1) * calc(n / 2 - 1)) % 10;
        } else { // 2n+1명 -> 마찬가지로 n+1명과 n명으로 쪼개서 계산
            result = (calc(n / 2 + 1) * calc(n / 2) + calc(n / 2) * calc(n / 2 - 1)) % 10;
        }
        dp.put(n, result);
        return result;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        dp.put(0, 0);
        dp.put(1, 1);
        dp.put(2, 2);
        dp.put(3, 3);

        System.out.println(calc(n));

        sc.close();
    }
}
