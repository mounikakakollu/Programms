package Arrays;

import java.util.*;

public class BubbleSort {
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int arr[] = new int[] {5,6,7,4,3,1};
		int len=arr.length;
        int temp;
        for(int i=0;i<len;i++) {
        	for(int j=0;j<len-1-i;j++) {
        		if(arr[j]>arr[j+1]) {
        			temp=arr[j];
        			arr[j]=arr[j+1];
        			arr[j+1]=temp;
        		}
        	}
        }
        System.out.println(Arrays.toString(arr));
	}
}
