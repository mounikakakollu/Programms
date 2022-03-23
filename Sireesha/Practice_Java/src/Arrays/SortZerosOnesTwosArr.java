package Arrays;
import java.util.*;
public class SortZerosOnesTwosArr {
    public void sort(int arr[]) {
    	int len=arr.length;
    	int ptr1=0,ptr2=0;
    	for(int i=0;i<len;i++) {
    		if(arr[i]==0)
    			ptr1++;
    		else if(arr[i]==1)
    			ptr2++;
    	}
    	for(int i=0;i<len;i++) {
    		if(i<ptr1)
    			arr[i]=0;
    		else if(i<ptr2+ptr1)
    			arr[i]=1;
    		else
    			arr[i]=2;
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
