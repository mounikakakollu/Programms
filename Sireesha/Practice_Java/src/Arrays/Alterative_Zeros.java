package Arrays;

public class Alterative_Zeros {

	
	public static void main(String[] args) {
		int arr[] =  new int[] {1,2,3,4,5};
		int len=arr.length;
		int newArr[]=new int[2*len];
		int var=0;
        for(int i=0;i<len;i++) {
        	newArr[var++] = arr[i];
        	newArr[var++] = 0;
        }
        System.out.println("Zeros at alteranative postions in a array:");
        for(int i=0;i<2*len;i++) {
        	System.out.print(newArr[i] + " ");
        }
	}
}
