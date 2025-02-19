
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;

public class Main {
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int n = Integer.parseInt(br.readLine());
    PriorityQueue<Integer> pq = new PriorityQueue<>();
    for(int i=0; i<n; i++) {
      int card = Integer.parseInt(br.readLine());
      pq.offer(card);
    }
    int answer = 0;
    while (pq.size() > 1) {
      int a = pq.poll();
      int b = pq.poll();
      pq.offer(a+b);
      answer += a+b;
    }
    System.out.println(answer);
  }

}

