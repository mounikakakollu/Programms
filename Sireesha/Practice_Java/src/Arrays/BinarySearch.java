package Arrays;
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
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int arr[] = new int[] {1,2,3,4,5};
		int ele=5;
	    Search s1= new Search();
        int k=s1.binarySearch(arr, 0, arr.length-1, ele);
  
        if(k == -1)
        	System.out.println("The element is not found");
        else
        	System.out.println("The element is found at index " + k);
        
	}
}
