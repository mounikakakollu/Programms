/**
 * 
 */
package arrays;

import java.util.ArrayList;
import java.util.List;


/**
 * @author mkakollu
 *
 */
public class PascalTriangle {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		int n = 5;
		List<Integer> pascalTriangle = new ArrayList<Integer>();
		List<Integer> indexes = new ArrayList<Integer>();
		List<Long> tmpList = null;
		for(Long tmp: tmpList) {
			System.out.println(tmp);
		}
		int startIndex = 0;
		pascalTriangle.add(1);
		indexes.add(0);
		for(int i=1; i<=n; i++) {
			indexes.add(indexes.get(i-1)+ i);
			startIndex = indexes.get(i-1);
			for(int j=0; j<=i; j++) {
				if(j== 0 || j == i) {
					pascalTriangle.add(1);
				}
				else {
					if(startIndex -1 >=0) {
						pascalTriangle.add(pascalTriangle.get(startIndex) + pascalTriangle.get(startIndex-1));
					}
				}
				startIndex +=1;
			}
			
		}

		startIndex = 0;
		for(int i=0; i<=n; i++) {
			for(int j=0; j<=i; j++, startIndex++) {
				System.out.print(pascalTriangle.get(startIndex) + " ");
			}
			System.out.println("");
			
		}

	}

}
