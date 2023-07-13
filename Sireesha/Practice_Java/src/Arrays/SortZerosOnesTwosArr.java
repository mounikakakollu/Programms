package Arrays;
/**
 * Sort the array in the order of 0's,1's and 2's
 */
import java.util.*;
public class SortZerosOnesTwosArr {
    public void sort(int arr[]) {
    	int len=arr.length;
    	int ptr1=0,temp;
    	for(int i=0;i<len;i++) {
    		if(arr[i]==0) {
    			temp=arr[i];
    			arr[i]=arr[ptr1];
    			arr[ptr1]=temp;
    			ptr1++;
    		}
    		    
    	}
    	int ptr2=ptr1;
    	for(int i=ptr1;i<len;i++) {
    		if(arr[i]==1) {
    			temp=arr[i];
    			arr[i]=arr[ptr2];
    			arr[ptr2]=temp;
    			ptr2++;
    		}
    	}
    
    }
	public static void main(String[] args) {
		// TODO Auto-generated method stub
        int arr[] = new int[] {0,1,2,2,1,0,0,0,1,2,1,2,0};
        System.out.println(Arrays.toString(arr));
        
        SortZerosOnesTwosArr obj=new SortZerosOnesTwosArr();
        obj.sort(arr);
        System.out.println("The sorted array " + Arrays.toString(arr));
	}

}
