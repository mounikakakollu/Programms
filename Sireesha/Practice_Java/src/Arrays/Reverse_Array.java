package Arrays;
import java.util.*;
public class Reverse_Array {
    
	public static void main(String[] args) {
		// TODO Auto-generated method stub
        int arr[] = new int[] {1,2,3,4,5,6};
        for(int i=0;i<arr.length/2;i++) {
        	int temp=arr[(arr.length-1)-i];
        	//System.out.println("temp" + temp);
        	arr[(arr.length-1)-i]=arr[i];
        	arr[i]=temp;
        }
        System.out.println("The Reversed array is:" + Arrays.toString(arr));
        
	}

}
