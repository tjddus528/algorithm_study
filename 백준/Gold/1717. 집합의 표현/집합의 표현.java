import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
  static int n, m;
  static int[] parent;
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());
    n = Integer.parseInt(st.nextToken());
    m = Integer.parseInt(st.nextToken());
    parent = new int[n+1];

    // 1. 초기화
    for(int i=0; i<n+1; i++) {
      parent[i] = i;
    }

    // 2. 질의 받기
    for(int i=0; i<m; i++) {
      st = new StringTokenizer(br.readLine());
      int q = Integer.parseInt(st.nextToken());
      int a = Integer.parseInt(st.nextToken());
      int b = Integer.parseInt(st.nextToken());
      if (q==0) {
        union(a, b);
      } else {
        System.out.println(checkSame(a, b));
      }
    }

  }

  // union(a,b)
  static void union(int a, int b) {
    a = find(a);
    b = find(b);
    parent[Math.max(a, b)] = Math.min(a, b);
  }
  // find(k) : 대표 노드 찾기
  static int find(int k) {
    if (parent[k] == k) return k;
    return parent[k] = find(parent[k]);
  }
  static String checkSame(int a, int b) {
    if (find(a) == find(b)) return "YES";
    else return "NO";
  }
}
