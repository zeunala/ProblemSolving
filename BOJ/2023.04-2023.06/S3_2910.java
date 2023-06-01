/*
빈도 정렬

입력
첫째 줄에 메시지의 길이 N과 C가 주어진다. (1 ≤ N ≤ 1,000, 1 ≤ C ≤ 1,000,000,000)
둘째 줄에 메시지 수열이 주어진다.

출력
첫째 줄에 입력으로 주어진 수열을 빈도 정렬한 다음 출력한다.

- N의 범위가 작으므로 문제의 요구사항을 그대로 구현한다.
* Pass/1st/00:19:41
*/
import java.util.*;
import java.util.stream.Collectors;

public class S3_2910 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int C = sc.nextInt();
        int[] arr = new int[N];

        for (int i = 0; i < N; i++) {
            arr[i] = sc.nextInt();
        }
        Map<Integer, Integer> countArr = new HashMap<>(); // 각 key값에 대하여 몇 번 나왔는지 체크
        Map<Integer, Integer> idxArr = new HashMap<>(); // 각 key값에 대하여 몇 번째에 처음 등장했는지 체크

        for (int i = 0; i < N; i++) {
            if (!countArr.containsKey(arr[i])) {
                countArr.put(arr[i], 0);
                idxArr.put(arr[i], i);
            }
            countArr.put(arr[i], countArr.get(arr[i]) + 1);
        }
        List<Integer> result = countArr.keySet()
                .stream()
                .sorted((a, b) -> {
                    if (countArr.get(a) == countArr.get(b)) {
                        return idxArr.get(a) - idxArr.get(b);
                    } else {
                        return countArr.get(b) - countArr.get(a);
                    }
                })
                .collect(Collectors.toList());

        for (Integer e : result) {
            for (int i = 0; i < countArr.get(e); i++) {
                System.out.print(e + " ");
            }
        }

        sc.close();
    }
}
