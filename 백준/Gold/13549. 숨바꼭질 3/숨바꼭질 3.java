import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;

public class Main {
  public static void main(String[] args) throws IOException {

    int[] visited = new int[100001];
    for (int i=0;i<100001;i++) visited[i] = -1;

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    String[] input = br.readLine().split(" ");
    int n = Integer.parseInt(input[0]);
    int k = Integer.parseInt(input[1]);
    int result = bfs(n, k, visited);

    System.out.println(result);
  }

  static int bfs(int n, int k, int[] visited) {
    visited[n] = 0;
    ArrayDeque<Integer> q = new ArrayDeque<>();
    q.add(n);
    while(!q.isEmpty()) {
      int now = q.poll();
      if (now == k) return visited[now];
      if (now*2 < 100001 && visited[now*2] < 0) {
        visited[now*2] = visited[now];
        q.add(now*2);
      }
      if (now-1 >= 0 && visited[now-1] < 0) {
        visited[now-1] = visited[now] + 1;
        q.add(now-1);
      }
      if (now+1 < 100001 && visited[now+1] < 0) {
        visited[now+1] = visited[now] + 1;
        q.add(now+1);
      }
      
    }
    return -1;
  }
}

