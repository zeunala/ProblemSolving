/*
프린터 큐

입력
첫 줄에 테스트케이스의 수가 주어진다. 각 테스트케이스는 두 줄로 이루어져 있다.
테스트케이스의 첫 번째 줄에는 문서의 개수 N(1 ≤ N ≤ 100)과,
몇 번째로 인쇄되었는지 궁금한 문서가 현재 Queue에서 몇 번째에 놓여 있는지를 나타내는 정수 M(0 ≤ M < N)이 주어진다.
이때 맨 왼쪽은 0번째라고 하자. 두 번째 줄에는 N개 문서의 중요도가 차례대로 주어진다.
중요도는 1 이상 9 이하의 정수이고, 중요도가 같은 문서가 여러 개 있을 수도 있다.

출력
각 테스트 케이스에 대해 문서가 몇 번째로 인쇄되는지 출력한다.

- 문서의 개수가 많지 않으므로, 문제 요구사항 그대로 구현해본다.
* Pass/1st/00:17:32
*/
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class S3_1966 {
    public static int maxValueOfQueue(Queue<Integer> queue) { // 큐에서 가장 큰 값 리턴
        int result = -1;

        for (Integer e : queue) {
            if (result < e) {
                result = e;
            }
        }

        return result;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();

        for (int i = 0; i < T; i++) {
            int N = sc.nextInt(); // 총 문서의 개수
            int M = sc.nextInt(); // 원하는 문서가 몇 번째에 있는지
            int answer = 1;
            Queue<Integer> queue = new LinkedList<>();

            for (int j = 0; j < N; j++) {
                queue.add(sc.nextInt());
            }

            while (queue.size() > 0) {
                int temp = queue.remove();

                if (maxValueOfQueue(queue) <= temp) { // 방금 꺼낸 큐의 값이 최댓값인 경우 (즉 그대로 꺼내면 되는 경우)
                    if (M == 0) { // 그리고 그게 처음 원했던 문서인 경우
                        System.out.println(answer);
                        break;
                    } else { // 아닌 경우 원하는 문서는 한 칸 앞으로 밀림
                        M--;
                        answer++;
                    }
                } else { // 최댓값이 아니라 다시 집어넣어야 하는 경우
                    queue.add(temp);

                    if (M == 0) {
                        M = queue.size() - 1;
                    } else {
                        M--;
                    }
                }
            }
        }

        sc.close();
    }
}
