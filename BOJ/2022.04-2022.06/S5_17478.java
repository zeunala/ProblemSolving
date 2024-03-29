/*
재귀함수가 뭔가요?

입력
교수님이 출력을 원하는 재귀 횟수 N(1 ≤ N ≤ 50)이 주어진다.

출력
출력 예시를 보고 재귀 횟수에 따른 챗봇의 응답을 출력한다.

- 입력에 따라 반복횟수를 두어 출력하면 될 것으로 보인다.
* Fail/1st/00:09:25
- 맨 첫줄은 반복을 하지 않도록 수정하였다.
* Fail/2nd/00:10:49
- 문제의 조건을 제대로 읽고 수정하였다.
* Pass/3rd/00:13:03
*/
import java.util.Scanner;

public class S5_17478 {
   static void printChat(int current, int end) { // 현재 current번째, 총 end번을 해야한다.
        String indent = "";
        for (int i = 1; i <= current; i++) {
            indent += "____";
        }

        if (current == end) {
            System.out.println(indent + "\"재귀함수가 뭔가요?\"");
            System.out.println(indent + "\"재귀함수는 자기 자신을 호출하는 함수라네\"");
            System.out.println(indent + "라고 답변하였지.");
        } else {
            System.out.println(indent + "\"재귀함수가 뭔가요?\"");
            System.out.println(indent + "\"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.");
            System.out.println(indent + "마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.");
            System.out.println(indent + "그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.\"");
            printChat(current + 1, end);
            System.out.println(indent + "라고 답변하였지.");
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        System.out.println("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.");
        printChat(0, N);
        sc.close();
    }
}
