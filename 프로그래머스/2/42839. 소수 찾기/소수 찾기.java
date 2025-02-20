import java.util.*;
class Solution {
    static int n;
    static int answer;
    static Set<Integer> results = new HashSet<>();
    public int solution(String numbers) {
        n = numbers.length();
        for(int r=1; r<=n; r++)
            dfs(numbers, new boolean[n], 0, new char[r], r);
        return results.size();
    }
    static boolean prime(int n) {
        if(n<=1) return false;
        for(int i=2; i<n; i++) {
            if(n%i==0) return false;
        }
        return true;
    }
    static void dfs(String origin, boolean[] visited, int depth, char[] num, int r) {
        if(depth == r) {
            int result = Integer.parseInt(String.valueOf(num));
            if (prime(result)) results.add(result);
            return;
        }
        for(int i=0; i< n; i++) {
            if (visited[i]) continue;
            visited[i] = true;
            num[depth] = origin.charAt(i);
            dfs(origin, visited, depth+1, num, r);
            visited[i] = false;
        }

        
    }
}