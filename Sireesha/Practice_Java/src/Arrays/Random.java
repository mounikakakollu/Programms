package Arrays;
import java.util.*;


public class Random {
    static Scanner s;
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		s =  new Scanner(System.in);
		int rand;
		System.out.println("Enter the array size:");
        int n = s.nextInt();
        int arr[] =  new int[n];
        System.out.println("Enter the array:");
        for(int i=0;i<n;i++) {
        	arr[i]=s.nextInt();
        }
        rand=(int)(Math.random()*(n-1));
        System.out.println("The value at generated index is:" + arr[rand]);
        
	}

}
