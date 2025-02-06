import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

  static int n, m, v;
  static ArrayList<Integer>[] graph;
  static boolean[] visited;
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());
    n = Integer.parseInt(st.nextToken());
    m = Integer.parseInt(st.nextToken());
    v = Integer.parseInt(st.nextToken());

    graph = new ArrayList[n+1];
    for(int i=1;i<n+1;i++) graph[i] = new ArrayList<>();
    for(int i=0;i<m;i++) {
      st = new StringTokenizer(br.readLine());
      int s = Integer.parseInt(st.nextToken());
      int e = Integer.parseInt(st.nextToken());
      graph[s].add(e);
      graph[e].add(s);
    }

    for(int i=1;i<n+1;i++) {
      Collections.sort(graph[i]);
    }

    visited = new boolean[n+1];
    dfs(v);
    System.out.println();
    visited = new boolean[n+1];
    bfs(v);
  }

  private static void dfs(int start) {
    visited[start] = true;
    System.out.print(start+" ");
    for (int node: graph[start]) {
      if (visited[node]) continue;
      dfs(node);
    }
  }

  private static void bfs(int start) {
    Queue<Integer> q = new LinkedList<>();
    q.offer(start);
    visited[start] = true;
    while (!q.isEmpty()) {
      int now = q.poll();
      System.out.print(now+" ");
      for(int node: graph[now]) {
        if (visited[node]) continue;
        visited[node] = true;
        q.offer(node);
      }
    }
  }

}
