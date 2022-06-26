/*
문자열 집합

입력
첫째 줄에 문자열의 개수 N과 M (1 ≤ N ≤ 10,000, 1 ≤ M ≤ 10,000)이 주어진다. 
다음 N개의 줄에는 집합 S에 포함되어 있는 문자열들이 주어진다.
다음 M개의 줄에는 검사해야 하는 문자열들이 주어진다.
입력으로 주어지는 문자열은 알파벳 소문자로만 이루어져 있으며, 길이는 500을 넘지 않는다.
집합 S에 같은 문자열이 여러 번 주어지는 경우는 없다.

출력
첫째 줄에 M개의 문자열 중에 총 몇 개가 집합 S에 포함되어 있는지 출력한다.

- 자바의 HashSet을 사용하면 쉽게 풀 수 있을 것으로 보인다.
* Pass/1st/00:17:01
*/
import java.util.*;

public class S3_14425 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();
        sc.nextLine();

        Set<String> stringSet = new HashSet<>();
        int answer = 0;

        for (int i = 0; i < N; i++)
            stringSet.add(sc.nextLine());
        
        for (int j = 0; j < M; j++) {
            if (stringSet.contains(sc.nextLine())) {
                answer++;
            }
        }

        System.out.println(answer);

        sc.close();
    }
}