package Arrays;

import java.util.*;

public class InsertionSort {
	public static void main(String[] args) {
		int arr[] = new int[] {6,7,4,3,2,1,0};
		int len=arr.length;
        int i,j,temp;
        for(i=1;i<len;i++) {
        	temp=arr[i];
        	j=i-1;
        	while(j>=0 && arr[j]>temp) {
        		arr[j+1]=arr[j];
        		j--;
        	}
        	arr[j+1]=temp;
        }
        System.out.println(Arrays.toString(arr));
	}
}
