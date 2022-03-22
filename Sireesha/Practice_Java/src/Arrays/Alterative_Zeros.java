package Arrays;

import java.util.Scanner;

public class Alterative_Zeros {

	static Scanner s;
	public static void main(String[] args) {
		s=new Scanner(System.in);
        System.out.println("Enter the array size:");
        int n = s.nextInt();
        int a[]= new int[n];
        System.out.println("Enter the array:");
        int i;
        for(i=0;i<n;i++) {
        	a[i]=s.nextInt();
        }
        for(i=0;i<n;i++) {
        	if(i%2==0) {
        		a[i]=0;
        	}
        }
        System.out.println("Zeros at even postions in a array:");
        for(i=0;i<n;i++) {
        	System.out.print(a[i] + " ");
        }

	}

}
