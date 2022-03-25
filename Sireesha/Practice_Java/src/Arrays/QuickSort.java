package Arrays;
import java.util.*;
/**
 * 
 * @author sireesha
 * Quick Sort
 *
 */
public class QuickSort {
    public void quickSort(int arr[],int l,int r) {
    	if(l<r) {
    		int p=partition(arr,l,r);
    		quickSort(arr,l,p-1);
    		quickSort(arr,p+1,r);
    	}
    	
    }
    public int partition(int arr[],int l,int r) {
    	int pivot=arr[r];
    	int j=l,i;
    	for(i=l;i<=r-1;i++) {
    		if(arr[i]<pivot) {
    			swap(arr,i,j);
    			j++;	
    		}
    	}
    	swap(arr,j,r);
    	return j;
    }
    public void swap(int arr[],int a,int b) {
    	int temp=arr[a];
    	arr[a]=arr[b];
    	arr[b]=temp;
    }
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int arr[] = new int[] {8,4,3,2,1,0,2,3};
		
		QuickSort obj = new QuickSort();
		obj.quickSort(arr,0,arr.length-1);
        System.out.println(Arrays.toString(arr));
	}

	
}
