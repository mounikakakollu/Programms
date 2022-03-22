package Arrays;
import java.util.*;
//assuming the given array is a sorted array
class Search{
	public int binarySearch(int arr[],int l,int r,int ele) {
		while(l<=r) {
			int mid=(l+r)/2;
			if(ele == arr[mid])
				return mid;
			else if(ele < arr[mid]) {
				return binarySearch(arr,l,mid-1,ele);
			}
			else {
				return binarySearch(arr,mid+1,r,ele); 
			}
		}
		return -1;
	}
}
public class BinarySearch {
    static Scanner s;
	public static void main(String[] args) {
		// TODO Auto-generated method stub
        s =  new Scanner(System.in);
        
		System.out.println("Enter the array size:");
        int n = s.nextInt();
        int arr[] =  new int[n];
        System.out.println("Enter the array in ascending order:");
        for(int i=0;i<n;i++) {
        	arr[i]=s.nextInt();
        }
        
        System.out.println("Enter the element to be searched:");
        int ele=s.nextInt();
        
        Search s1= new Search();
        int k=s1.binarySearch(arr, 0, arr.length-1, ele);
  
        if(k == -1)
        	System.out.println("The element is not found");
        else
        	System.out.println("The element is found at index " + k);
        
	}
}
