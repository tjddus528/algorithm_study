import java.util.Scanner;

public class Main {

  public static void main(String[] args) {

    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    String numbers = sc.next();
    char[] numList = numbers.toCharArray();

    int result = 0;
    for (int i = 0; i < n; i++) {
      result += numList[i] - '0';
    }
    System.out.println(result);
  }
}