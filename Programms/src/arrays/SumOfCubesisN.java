/**
 * 
 */
package arrays;

import java.util.Arrays;

/**Count pairs (a, b) whose sum of cubes is N (a^3 + b^3 = N)
 * Given N, count all ‘a’ and ‘b’ that satisfy the condition a^3 + b^3 = N. 
 * @author mkakollu
 *
 */
public class SumOfCubesisN {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		int n = 9;
		int i=1;
		int j= (int) Math.cbrt(n);
		while(i<=j) {
			int tmp = (int) (Math.pow(i, 3) +(int) Math.pow(j, 3)) ;
//			System.out.println(i + " " + j + " " + Math.pow(n, 1/3));
			if(tmp== n) {
				System.out.println(i + " " + j);
				System.out.println(j + " " + i);
				i++;
				j-=1;
			}
			if(tmp<n)
				i+=1;
			else {
				j-=1;
			}
		}

	}

}
