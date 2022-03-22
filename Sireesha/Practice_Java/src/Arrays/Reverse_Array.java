package Arrays;
import java.util.Scanner;
public class Reverse_Array {
    
	static Scanner s;
	public static void main(String[] args) {
		// TODO Auto-generated method stub
        s=new Scanner(System.in);
        System.out.println("Enter the array size:");
        int n = s.nextInt();
        int a[]= new int[n];
        System.out.println("Enter the array:");
        int i,temp;
        for(i=0;i<n;i++) {
        	a[i]=s.nextInt();
        }
        for(i=0;i<n/2;i++) {
        	temp=a[(n-1)-i];
        	//System.out.println("temp" + temp);
        	a[(n-1)-i]=a[i];
        	a[i]=temp;
        }
        System.out.println("The Reversed array is:");
        for(i=0;i<n;i++) {
        	System.out.print(a[i] + " ");
        }
	}

}
