import java.util.Scanner;

/*
재귀함수가 뭔가요?

입력
교수님이 출력을 원하는 재귀 횟수 N(1 ≤ N ≤ 50)이 주어진다.

출력
출력 예시를 보고 재귀 횟수에 따른 챗봇의 응답을 출력한다.

- 입력에 따라 반복횟수를 두어 출력하면 될 것으로 보인다.
* Fail/1st/00:09:25
*/
public class S5_17478 {
   static void printChat(int current, int end) { // 현재 current번째, 총 end번을 해야한다.
        if (current > end)
            return;

        String indent = "";
        for (int i = 1; i <= current; i++) {
            indent += "____";
        }

        System.out.println(indent + "어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.");
        System.out.println(indent + "\"재귀함수가 뭔가요?\"");
        System.out.println(indent + "\"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.");
        System.out.println(indent + "마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.");
        System.out.println(indent + "그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.\"");
        printChat(current + 1, end);
        System.out.println(indent + "라고 답변하였지.");
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        printChat(0, N);
        sc.close();
    }
}
