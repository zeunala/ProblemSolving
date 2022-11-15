/*
DNA

입력
첫 줄에 DNA의 수 N과 문자열의 길이 M이 주어진다.
그리고 둘째 줄부터 N+1번째 줄까지 N개의 DNA가 주어진다.
N은 1,000보다 작거나 같은 자연수이고, M은 50보다 작거나 같은 자연수이다.

출력
첫째 줄에 Hamming Distance의 합이 가장 작은 DNA 를 출력하고,
둘째 줄에는 그 Hamming Distance의 합을 출력하시오.
그러한 DNA가 여러 개 있을 때에는 사전순으로 가장 앞서는 것을 출력한다.

- n번째 문자들에 대해 가장 많은 알파벳이 결과 DNA의 알파벳이 된다.
만약 가장 많은 알파벳이 여러개라면 사전순으로 가장 앞서도록 A, C, G, T 순으로 우선순위를 갖도록 한다.
* Pass/1st/00:24:38
*/
import java.util.*;

public class S5_1969 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt(); // DNA의 수
        int M = sc.nextInt(); // 문자열의 길이
        List<String> allDNA = new ArrayList<>();
        StringBuilder answer = new StringBuilder(); // 결과 문자열
        int distance = 0; // 거리의 합

        sc.nextLine(); // 개행 문자 제거
        for (int i = 0; i < N; i++) {
            allDNA.add(sc.nextLine());
        }

        for (int i = 0; i < M; i++) {
            Map<Character, Integer> alphaCount = new LinkedHashMap<>(); // A, C, G, T 별로 존재 횟수
            alphaCount.put('A', 0);
            alphaCount.put('C', 0);
            alphaCount.put('G', 0);
            alphaCount.put('T', 0);

            for (int j = 0; j < N; j++) {
                char temp = allDNA.get(j).charAt(i); // j번째 문자열의 i번째 알파벳
                alphaCount.put(temp, alphaCount.get(temp) + 1);
            }

            int maxCount = Collections.max(alphaCount.values());
            for (Character alpha : alphaCount.keySet()) {
                if (alphaCount.get(alpha) == maxCount) {
                    answer.append(alpha);
                    distance += N - maxCount;
                    break;
                }
            }
        }

        System.out.println(answer.toString());
        System.out.print(distance);

        sc.close();
    }
}
