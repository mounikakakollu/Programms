package leetCode;

/**
 * Problem 1 
 * @author mkakollu
 *
 */
public class EditDistance {
	
	public static int getMin(int val1, int val2, int val3) {
		if(val1<val2 && val1<val3)
			return val1;
		if(val2<val3)
			return val2;
		return val3;
	}
	
	public static String getSubStr(String str) {
		return str.substring(0,str.length()-1);
	}

	public static int editDistance(String str1, String str2) {
		if(str1.isEmpty())
			return str2.length();
		if(str2.isEmpty())
			return str1.length();
		if(str1.charAt(str1.length()-1) == str2.charAt(str2.length()-1))
			return editDistance(getSubStr(str1), getSubStr(str2));
		else {
			return 1 + getMin(
					editDistance(getSubStr(str1), str2),
					editDistance(str1, getSubStr(str2)),
					editDistance(getSubStr(str1), getSubStr(str2))
					);
			
		}
	}

	
	public static void main(String[] args) {
		String str1 = "horse";
		String str2 = "ros";
		System.out.println(editDistance(str1, str2));
	}
}
