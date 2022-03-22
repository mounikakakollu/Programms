package Arrays;

import java.util.Scanner;

public class SelectionSort{
		static Scanner s;
		public static void main(String[] args) {
			// TODO Auto-generated method stub
			s =  new Scanner(System.in);
			System.out.println("Enter the array size:");
	        int n = s.nextInt();
	        int arr[] =  new int[n];
	        System.out.println("Enter the array:");
	        for(int i=0;i<n;i++) {
	        	arr[i]=s.nextInt();
	        }
	        int temp,min_index;
	        for(int i=0;i<n-1;i++) {
	        	min_index=i;
	        	for(int j=i+1;j<n;j++) {
	        		if(arr[i]>arr[j]) {
	        			min_index=j;
	        		}
	        	}
	        	temp=arr[min_index];
    			arr[min_index]=arr[i];
    			arr[i]=temp;
	        }
	        for(int i=0;i<n;i++) {
	        	System.out.println(arr[i]);
	        }
	}
}
