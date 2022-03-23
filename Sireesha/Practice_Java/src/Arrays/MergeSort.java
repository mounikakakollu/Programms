package Arrays;
import java.util.*;

public class MergeSort {  
	public void mergeSort(int arr[],int l,int r){
		if(l<r) {
		int mid=l+(r-l)/2;
		mergeSort(arr,l,mid);
	    mergeSort(arr,mid+1,r);
	    merge(arr,l,mid,r);
	    } 
    }
    public void merge(int arr[],int l,int m,int r) {
    	int len1=m+1-l;
    	int len2=r-m;
    	int leftArr[] = new int[len1];
    	int rightArr[] = new int[len2];
    	for(int i=0;i<len1;i++) {
    		leftArr[i]=arr[l+i];
    	}
    	for(int j=0;j<len2;j++) {
    		rightArr[j]=arr[m+1+j];
    	}
    	int i=0,j=0,k=l;
    	while(i<len1 && j<len2) {
    		if(leftArr[i]>rightArr[j])
    			arr[k++]=rightArr[j++];
    		else
    			arr[k++]=leftArr[i++];
    	}
    	while(i<len1) {
    		arr[k++]=leftArr[i++];
    	}
    	while(j<len2) {
    		arr[k++]=rightArr[j++];
    	}
	}
	public static void main(String[] args) {
		// TODO Auto-generated method stub
         int arr[] = new int[] {1,2,5,6,7,4,3,2,1};
         System.out.println("The Array is " + Arrays.toString(arr));
         
         MergeSort obj=new MergeSort();
         obj.mergeSort(arr,0,arr.length-1);
         System.out.println("The Sorted Array is " + Arrays.toString(arr));
	}
}
