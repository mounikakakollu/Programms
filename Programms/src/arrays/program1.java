package main;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import com.sun.prism.impl.Disposer.Target;

/**
 * 
 * given arr = [4,3,6,2,8,9]
 * target = 11
 *
 *tmp = {4:[1]}
 *
 * sorted_arr = sort(arr)
 * 9+2 = 11
 * i = 0
 * j = len(arr) -1
 * 2 3 4 6 8 9 10
 * 
 * 
 *output -> indexes of two number which gives target
 */

public class program1 {
	
	public static void main(String[] args) {
		 List<Integer> arr = Arrays.asList(4,4,2,6,3);
		 int target = 7;
		 Map<Integer, List<Integer>> bufferMap = new HashMap<Integer, List<Integer>>();
		 for(int i=0; i< arr.size(); i++) {
			 if(bufferMap.containsKey(arr.get(i))) {
				 List<Integer> tmp = bufferMap.get(arr.get(i));
				 tmp.add(i);
				 bufferMap.put(arr.get(i), tmp);
			 }
			 else {
				 List<Integer> tmp = new ArrayList<Integer>();
				 tmp.add(i);
				 bufferMap.put(arr.get(i), tmp);
			 }
			 int diff;
			 if(target > arr.get(i))
				 diff = target - arr.get(i);
			 else
				 diff = arr.get(i) - target;
			 if(bufferMap.containsKey(diff)) {
					
				 if(diff == arr.get(i) && bufferMap.get(arr.get(i)).size()>1) {
					 System.out.println(bufferMap.get(arr.get(i)).get(0) + " " + bufferMap.get(arr.get(i)).get(1));
				 }
				 else if(diff !=arr.get(i)) {
					 System.out.println(bufferMap.get(arr.get(i)).get(0) + " " + bufferMap.get(diff).get(0));
				 }
			}
		 }
	}
		 
//		 int i = 0;
//		 int j = arr.size() -1;
//		 int target = 6;
//		 while(i<j) {
//			 int currSum = arr.get(i) + arr.get(j);
//			 if(currSum > target) {
//				 j -=1;
//			 }
//			 else if(currSum < target) {
//				 i+=1;
//			 }
//			 else {
//				 break;
//			 }
//		 }
//		 if(i>=j) {
//			 System.out.println("Not found");
//		 }
//		 System.out.println("Indexes of two numbers are: " + i + " " + j);
//	}

}
