/*
귀걸이

입력
입력은 번호를 가진 시나리오들로 구성됩니다. 시나리오 번호는 1부터 순서대로 증가하고, 각 시나리오는 아래의 내용을 포함합니다.

한 줄에 귀걸이를 압수당한 여학생의 수, n (1 ≤ n ≤ 100)이 주어집니다.
다음 n줄에 걸쳐 여학생들의 이름(최대 60자)이 주어집니다.
다음 2n − 1줄에 여학생 번호와 'A' 또는 'B'가 공백을 사이에 두고 주어집니다.
번호는 교감선생님의 여학생 이름 리스트와 순서가 일치합니다.
즉, 1은 첫 번째로 압수당한 여학생입니다. 여학생 번호는 최대 2번 등장하며,
두 번째로 등장할 때는 첫 번째 경우와 다른 'A' 또는 'B'가 뒤에 적힙니다.
번호가 처음 등장하는 것은 압수되었음을, 두 번째로 등장하는 것은 돌려받았음을 의미합니다.
'0'을 마지막 줄로 하여 입력이 종료됩니다. '0'은 처리하지 않습니다.

출력
시나리오 번호와 귀걸이를 돌려받지 못한 여학생의 이름을 공백으로 구분하여 한 줄씩 출력하십시오.

- A집합과 B집합을 만들면, 두 집합의 차집합이 돌려받지 못한 여학생의 이름이 된다.
* Pass/1st/00:26:41
- 습관적으로 파이썬에서처럼 문자열을 equals가 아닌 ==로 비교하는 실수로 인해 시간이 오래걸렸다.
파이썬에서처럼 풀이하는 실수를 줄여야할 것으로 보인다.
*/
import java.util.*;

public class S5_1380 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int caseNum = 1; // 시나리오 번호

        while (true) {
            int studentNum = Integer.parseInt(sc.nextLine());
            List<String> idxToName = new ArrayList<>(); // idxToName.get(i)는 i번째(i>=1) 여학생의 이름
            Set<Integer> setA = new HashSet<>();
            Set<Integer> setB = new HashSet<>();

            idxToName.add("None");

            if (studentNum == 0) {
                break;
            }

            // 여학생의 이름을 입력 받음
            for (int i = 0; i < studentNum; i++) {
                idxToName.add(sc.nextLine());
            }

            // 각 번호별로 A, B 집합에 넣음
            for (int i = 0; i < 2 * studentNum - 1; i++) {
                String[] temp = sc.nextLine().split(" ");

                if (temp[1].equals("A")) {
                    setA.add(Integer.parseInt(temp[0]));
                } else {
                    setB.add(Integer.parseInt(temp[0]));
                }
            }
            
            // 차집합을 구하고 남은 원소 한 개의 이름을 시나리오 번호와 함께 출력
            if (setA.size() > setB.size()) {
                setA.removeAll(setB);
                System.out.println(caseNum + " " + idxToName.get((Integer)setA.toArray()[0]));
            } else {
                setB.removeAll(setA);
                System.out.println(caseNum + " " + idxToName.get((Integer)setB.toArray()[0]));
            }

            caseNum++;
        }
        
        sc.close();
    }
}
