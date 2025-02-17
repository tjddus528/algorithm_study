import java.util.*;

class Solution {
    public int solution(int[] nums) {
        Map<Integer, Integer> map = new HashMap<>();
        for(int num: nums)
            map.put(num, map.getOrDefault(num, 0)+1);
        int n = nums.length;
        if (map.size() >= n/2) return n/2;
        else return map.size();
    }
}