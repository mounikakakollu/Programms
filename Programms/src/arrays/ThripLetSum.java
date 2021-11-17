package arrays;

import java.util.ArrayList;
import java.util.List;

public class ThripLetSum {
	
	public int partition(List<Integer>array, int start, int end) {
		int pivot = array.get(end);
		int i = start -1;
		for(int j = start; j<end; j++) {
			if(array.get(j)<pivot) {
				i++;
				int tmp = array.get(i);
				array.set(i, array.get(j));
				array.set(j, tmp);
			}
		}
		i++;
		int tmp = array.get(i);
		array.set(i, array.get(end));
		array.set(end, tmp);
		return i;
	}
	
	public void quickSort(List<Integer>array,int start, int end) {
		if(start<end) {
			int pivot = partition(array, start, end);
			quickSort(array, start, pivot-1);
			quickSort(array, pivot, end);
		}
		
	}

	public static void main(String[] args) {
		List<Integer> array = new ArrayList<Integer>();
		for(int i=0; i<args.length; i++) {
			array.add(Integer.parseInt(args[i]));
		}
		ThripLetSum obj = new ThripLetSum();
		obj.quickSort(array, 0, array.size()-1);
		array.forEach(ele -> {
			System.out.print(ele);
		});
		int sum = 11;
		for(int i=0; i<array.size(); i++) {
			int j=i+1;
			int k = array.size()-1;
			while(j<k) {
				int currentSum = array.get(i) + array.get(j) + array.get(k);
				if(sum == currentSum)
					break;
				else if(sum<currentSum)
					k--;
				else
					j++;
			}
			if(j<k) {
				System.out.println(String.format("Triplet found : %d, %d, %d" , array.get(i), array.get(j), array.get(k)));
			}
		}
		

	}

}
