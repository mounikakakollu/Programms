package arrays;
import java.util.Arrays;

/** Reverse the given Array
 * 
 * @author mounika
 *
 */

public class ReverseTheArray {

  public String[] reverse(String[] arr) {
    int i=0;
    int j = arr.length-1;
    while(i<j) {
      String tmp = arr[i];
      arr[i] = arr[j];
      arr[j] = tmp;
      i++;
      j--;
    }
    return arr;
  }
  public static void main(String args[]) {
    ReverseTheArray obj = new ReverseTheArray();
    String[] result = obj.reverse(args);
    Arrays.asList(result).forEach(ele -> {
    	System.out.print(ele);
    });
  }
}
