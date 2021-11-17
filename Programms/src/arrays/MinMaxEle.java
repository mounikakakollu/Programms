/**
 * 
 */
package arrays;

/**
 * To find minimum and maximum element in an array
 * @author mounika
 *
 */
public class MinMaxEle {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		MinMaxEle obj = new MinMaxEle();
		Integer[] minMax = obj.findMinMaxEle(args);
		System.out.println("Minimum element in the array is : " + minMax[0]);
		System.out.println("Maximum element in the array is : " + minMax[1]);
	}
	
	public Integer[] findMinMaxEle(String[] args) {
		Integer min = Integer.parseInt(args[0]);
		Integer max = Integer.parseInt(args[0]);
		int i=0;
		int j=args.length -1 ;
		while(i<j) {
			if(Integer.parseInt(args[i]) < min) {
				min =Integer.parseInt( args[i]);
			}
			else if(Integer.parseInt(args[i])> max) {
				max = Integer.parseInt(args[i]);
			}
			
			if(Integer.parseInt(args[j]) < min) {
				min = Integer.parseInt(args[j]);
			}
			else if(Integer.parseInt(args[j])> max) {
				max = Integer.parseInt(args[j]);
			}
			i++;
			j--;
			
		}
		Integer[] result = new Integer[2];
		result[0] = min;
		result[1] = max;
		return result;
		
		
	}

}
