package Arrays;

import java.util.*;

public class SelectionSort{
		
		public static void main(String[] args) {
			int [] arr =  new int[] {5,6,7,4,3,2};
	        int temp,min_index;
	        for(int i=0;i<arr.length-1;i++) {
	        	min_index=i;
	        	for(int j=i+1;j<arr.length;j++) {
	        		if(arr[min_index]>arr[j]) {
	        			min_index=j;
	        		}
	        	}
	        	temp=arr[min_index];
    			arr[min_index]=arr[i];
    			arr[i]=temp;
	        }
	        System.out.println("The sorted array is " + Arrays.toString(arr));
	}
}
