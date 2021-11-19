/**
 * 
 */
package strings;

import java.util.Arrays;
import java.util.List;

/**Find the largest sum subarray (kadaney's algorithm)


 * @author mkakollu
 *
 */
public class MaxSumSubArray {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		List<Integer> array = Arrays.asList(-4,2,-5,2,-1,3,6,-5,1);
		int maxSum = array.get(0);
		int curMaxSum = array.get(0);
		int start = 0;
		int end = 0;
		for(int i=0; i<array.size(); i++) {
			if(array.get(i) > array.get(i)+curMaxSum)  {
				curMaxSum = array.get(i);
				start = i;
			}
			else {
				curMaxSum +=array.get(i);
			}
			if(maxSum<curMaxSum) { 
				maxSum = curMaxSum;
				end = i;
			}
		}
		System.out.println(maxSum);
		System.out.println(array.subList(start, end+1));
	}

}
