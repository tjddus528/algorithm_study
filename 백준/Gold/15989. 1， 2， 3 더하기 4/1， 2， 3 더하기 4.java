import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
  public static void main(String[] args) throws IOException {
    int[] dp = new int[10001];
    for (int i=0;i<10001;i++) dp[i] = 1;

    for (int i=2;i<10001;i++) dp[i] += dp[i-2];
    for (int i=3;i<10001;i++) dp[i] += dp[i-3];

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int t = Integer.parseInt(br.readLine());

    for (int i=0;i<t;i++) {
      int n = Integer.parseInt(br.readLine());
      System.out.println(dp[n]);
    }
  }
}
