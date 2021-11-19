/**
 * 
 */
package arrays;

import java.util.Arrays;
import java.util.List;

/**Partition problem is to determine whether a given set can be partitioned into two subsets 
 * such that the sum of elements in both subsets is the same.
 * @author mkakollu
 *
 */
public class EqualSumSubArrays {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		List<Integer> array = Arrays.asList(1,3,5,3,2);
		int sum = 0;
		for(int i=0; i<array.size();  i++) {
			sum+=array.get(i);
		}
		if(sum%2 != 0) {
			System.out.println("Array can't be partitioned into to equal subArrays with same sum");
			return;
		}
		Boolean[] tmp = new Boolean[sum/2 +1];
		for(int i=0; i<=sum/2; i++) {
			tmp[i] = false;
		}
		for(int i=0; i<array.size(); i++) {
			for (int j=sum/2; j>=array.get(i); j--) {
				if(tmp[j-array.get(i)] == true || j== array.get(i))
					tmp[j] = true;
			}
		}
		if(tmp[sum/2] == true)
			System.out.println("Array can be partitioned into two equal subArrays");
		else
			System.out.println("Array can't be partitioned into to equal subArrays with same sum");

	}

}
