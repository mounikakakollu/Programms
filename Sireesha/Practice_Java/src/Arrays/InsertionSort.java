package Arrays;

import java.util.Scanner;

public class InsertionSort {
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
        int i,j,temp;
        for(i=1;i<n;i++) {
        	temp=arr[i];
        	j=i-1;
        	while(j>=0 && arr[j]>temp) {
        		arr[j+1]=arr[j];
        		j--;
        	}
        	arr[j+1]=temp;
        }
        for(i=0;i<n;i++) {
        	System.out.println(arr[i]);
        }
	}

}
