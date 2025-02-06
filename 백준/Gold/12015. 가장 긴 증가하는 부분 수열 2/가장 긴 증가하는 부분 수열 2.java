import java.io.*;
import java.util.Arrays;

public class Main {

  static int[] list;
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int n = Integer.parseInt(br.readLine());
    int[] arr = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
    list = new int[n];
    list[0] = arr[0];
    int i = 1;
    int j = 0;
    while (i < n) {
      if (arr[i] > list[j]) {
        list[j+1] = arr[i];
        j ++;
      } else {
        int idx = binarySearch(0, j, arr[i]);
        list[idx] = arr[i];
      }
      i++;
    }
    System.out.println(j+1);
  }

  private static int binarySearch(int left, int right, int target) {
    while(left < right) {
      int mid = (left + right) / 2;
      if (list[mid] < target) left = mid + 1;
      else right = mid;
    }
    return right;
  }

}
