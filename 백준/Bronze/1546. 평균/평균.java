import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Main {
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    int n = Integer.parseInt(br.readLine());
    StringTokenizer st = new StringTokenizer(br.readLine());
    int max = 0;
    int sum = 0;
    for (int i=0;i<n;i++) {
      int num = Integer.parseInt(st.nextToken());
      if (num > max) max = num;
      sum += num;
    }
    System.out.println(sum*100.0 / max / n);
  }
}
