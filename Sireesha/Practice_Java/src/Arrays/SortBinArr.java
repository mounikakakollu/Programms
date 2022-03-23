package Arrays;
import java.util.*;
public class SortBinArr {
    public void sort(int arr[]) {
    	int j=arr.length;
    	for(int i=arr.length-1;i>=0;i--) {
    		if(arr[i]==1) {
    			j--;
    			int temp=arr[i];
    			arr[i]=arr[j];
    			arr[j]=temp;
    		}
    			
    	}
    }
	public static void main(String[] args) {
		// TODO Auto-generated method stub
        int arr[]=new int[] {1,0,1,1,0,1,0,1};
        
        SortBinArr obj=new SortBinArr();
        obj.sort(arr);
        System.out.println(Arrays.toString(arr));
	}
}
