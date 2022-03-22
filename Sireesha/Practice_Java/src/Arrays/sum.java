package Arrays;

import java.util.Scanner;
public class sum {
    static Scanner s; 
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		s=new Scanner(System.in);
		System.out.println("Enter the array size:");
		int n = s.nextInt();
		int a[] = new int[n];
		int i,sum=0;
		System.out.println("Enter the array:");
		for(i=0;i<n;i++) {
			a[i]=s.nextInt();
		}
		
		for(i=0;i<n;i++) {
			sum=sum+a[i];
		}
        System.out.println("The sum of the array is " + sum);
	}

}
