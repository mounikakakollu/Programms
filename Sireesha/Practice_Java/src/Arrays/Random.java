package Arrays;



public class Random {
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int arr[] = new int[] {1,2,3,6,7,8};
        int rand=(int)(Math.random()*(arr.length-1));
        System.out.println("The value at generated index is:" + arr[rand]);
        
	}

}
