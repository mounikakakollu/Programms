package Arrays;

public class sum {
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int arr[] = new int[] {1,2,3,4,5,6};
		int sum=0;
		
		for(int i=0;i<arr.length;i++) {
			sum=sum+arr[i];
		}
        System.out.println("The sum of the array is " + sum);
	}

}
