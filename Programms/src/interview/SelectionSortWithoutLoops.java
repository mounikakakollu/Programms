package interview;

import java.util.ArrayList;

public class SelectionSortWithoutLoops {
	
	public void sort(ArrayList<Integer> array, int index, int size, int currEle, int min, int minEleIndex) {
		
		if(array.isEmpty())
			return;
		if(currEle >=size)
			return;
		if(index>=size) {
			array.set(minEleIndex, array.get(currEle));
			array.set(currEle, min);
			if(currEle+1 <size)
				sort(array, currEle+1, size, currEle+1, array.get(currEle+1), currEle+1);
		}
		else if(min> array.get(index)) {
			sort(array, index+1, size, currEle, array.get(index), index);
		}
		else 
			sort(array, index+1, size, currEle, min, minEleIndex);
	}
	
	public static void  main(String[] args) {
		ArrayList<Integer> array = new ArrayList();
		array.add(4);
		array.add(3);
		array.add(2);
		array.add(1);
		array.add(10);
		SelectionSortWithoutLoops obj = new SelectionSortWithoutLoops();
		int n = array.size();
		obj.sort(array,0,n, 0, array.get(0),0);
		for(int i=0; i<n; i++) {
			System.out.print(array.get(i)+" ");
		}
		System.out.println();
		
	}

}
