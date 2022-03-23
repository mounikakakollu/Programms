package Arrays;

import java.util.Scanner;
//chegg answer
public class numbers {
	static Scanner s;

	public static void main(String[] args) {
		// Scanner is used to take input from the user
		s=new Scanner(System.in);
        System.out.println("You had to enter n values before both a and b were seen:");
        // a and b values are taken as the inputs
        int a = s.nextInt();
        int b = s.nextInt();
        // flag1 and flag2 are used to compare the inputs values with a and b
        //count is used to store the total numers are given
        int flag1 = 0, flag2= 0 , count=0;
        while(flag1!=1 || flag2!=1) {
        	int n=s.nextInt();
        	count++;
        	if(n == a)
        		flag1=1;
        	else if(n==b)
        		flag2=1;
        }
        System.out.println("You had to enter " + count + " values before both " + a + " and " + b + " were seen.");

	}

}
