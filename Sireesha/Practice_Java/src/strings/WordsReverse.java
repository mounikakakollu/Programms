package strings;

public class WordsReverse {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String str="Hello world";
		System.out.println(str);
		String arr[]=str.split(" ");
		for(int i=0;i<arr.length;i++) {
			int len=arr[i].length()-1;
			String reverseWord="";
			while(len>=0) {
				reverseWord=reverseWord+arr[i].charAt(len);
				len--;
			}
			arr[i]=reverseWord;
		}
		String strNew="";
        for(int i=0;i<arr.length;i++) {
        	strNew=strNew+arr[i]+" ";
        }
        System.out.println("The reversed array is " + strNew);
	}

}
