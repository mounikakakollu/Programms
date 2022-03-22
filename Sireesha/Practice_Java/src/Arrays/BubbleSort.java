package Arrays;

import java.util.Scanner;

public class BubbleSort {
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
        int temp;
        for(int i=0;i<n;i++) {
        	for(int j=0;j<n-1-i;j++) {
        		if(arr[j]>arr[j+1]) {
        			temp=arr[j];
        			arr[j]=arr[j+1];
        			arr[j+1]=temp;
        		}
        	}
        }
        for(int i=0;i<n;i++) {
        	System.out.println(arr[i]);
        }
	}
}
