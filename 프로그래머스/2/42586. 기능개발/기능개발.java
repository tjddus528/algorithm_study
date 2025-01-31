import java.util.*;
class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        List<Integer> answer = new ArrayList<>(); 
        List<Integer> days = new ArrayList<>(); 
        Stack<Integer> stack = new Stack<>();
        
        for (int i=0;i<progresses.length;i++) {
            int day = (int)Math.ceil((100.0-progresses[i]) / speeds[i]);
            days.add(day);
        }
        
        stack.add(days.get(0));
        int cnt = 1;
        for(int i=1;i<days.size();i++) {
            if (stack.peek() < days.get(i)) {
                stack.add(days.get(i));
                answer.add(cnt);
                cnt = 1;
            } else {
                cnt ++;
            }
        }
        answer.add(cnt);
        
        int[] res = answer.stream().mapToInt(i -> i).toArray();
        return res;
    }
}