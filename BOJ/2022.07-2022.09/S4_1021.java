/*
회전하는 큐

입력
첫째 줄에 큐의 크기 N과 뽑아내려고 하는 수의 개수 M이 주어진다.
N은 50보다 작거나 같은 자연수이고, M은 N보다 작거나 같은 자연수이다.
둘째 줄에는 지민이가 뽑아내려고 하는 수의 위치가 순서대로 주어진다. 위치는 1보다 크거나 같고, N보다 작거나 같은 자연수이다.

출력
첫째 줄에 문제의 정답을 출력한다.

- 어떤 방식으로 움직이든 각 단계 이후 큐의 상태는 같으므로 그리디 알고리즘을 사용하여 해결할 수 있다.
* Pass/1st/00:19:19
*/
import java.util.*;

public class S4_1021 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();

        Queue<Integer> queueArr = new LinkedList<>();
        int answerCount = 0;

        for (int i = 1; i <= N; i++)
            queueArr.add(i);

        for (int i = 0; i < M; i++) {
            int target = sc.nextInt();

            // 한 쪽 방향으로만 돌려서 총 몇 번만에 제거할 수 있는지 찾는다.
            int tempCount = 0;
            while (true) {
                int temp = queueArr.remove();

                if (temp == target)
                    break;

                tempCount++;
                queueArr.add(temp);
            }

            // 기존 있던 원소 개수에서 한 쪽 방향으로만 돌렸을 때 횟수를 빼면 다른 방향으로 돌렸을 때 횟수가 나온다.
            answerCount += Math.min(tempCount, queueArr.size() + 1 - tempCount);
        }

        System.out.println(answerCount);
        
        sc.close();
    }
}
