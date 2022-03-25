package Arrays;

import java.util.*;
/**
 * 
 * @author sireesha
 * print the pairs of the numbers whose sum is equal to given target sum.
 *
 */
public class SumPairs {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int arr[]= new int[] {0,8,9,1,2,3,4,5};
		int target=5;
		MergeSort obj=new MergeSort();
		obj.mergeSort(arr, 0, arr.length-1);
		System.out.println(Arrays.toString(arr));
		
		int ptr1=0,ptr2=arr.length-1;
		while(ptr1<ptr2) {
			int sum=arr[ptr1]+arr[ptr2];
			if( sum == target)
				System.out.println("{" + arr[ptr1] + "," + arr[ptr2] + "}");
			if(sum>target)
				ptr2--;
			else
				ptr1++;
		}

	}

}
