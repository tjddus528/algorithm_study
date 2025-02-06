import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
  public static class Data {
    int t, p;
    public Data(int t, int p) {
      this.t = t;
      this.p = p;
    }
    @Override
    public String toString() {
      return "t:"+t+", p:"+p;
    }
  }

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int n = Integer.parseInt(br.readLine());
    Data[] consult = new Data[n+1];
    for(int i=1;i<n+1;i++) {
      StringTokenizer st = new StringTokenizer(br.readLine());
      int t = Integer.parseInt(st.nextToken());
      int p = Integer.parseInt(st.nextToken());
      consult[i] = new Data(t, p);
    }

    int[] dp = new int[n+2];
    dp[n+1] = 0;
    if (n + consult[n].t <= n+1) {
      dp[n] = consult[n].p;
    } else {
      dp[n] = 0;
    }
    for(int i=n-1;i>0;i--) {
      if (i + consult[i].t <= n+1) {
        dp[i] = Math.max(consult[i].p + dp[i+consult[i].t], dp[i+1]);
      } else {
        dp[i] = dp[i+1];
      }
    }
    System.out.println(dp[1]);
  }

}
