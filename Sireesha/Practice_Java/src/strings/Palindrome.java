package strings;

/**
 * 
 * @author Sireesha
 * The program is find to given string is palindrome or not.
 *
 */
public class Palindrome {
	public void palindrome(String str) {
		int flag=0;
		for(int i=0;i<str.length()/2;i++) {
			if((str.charAt(i)) != (str.charAt(str.length()-1-i))) {
				flag=1;
			    break;
			}
		}
		if(flag == 0)
		     System.out.println("Its a palindrome");
		else
			System.out.println("Its not a palindrome");
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String str="radaR";
		
		Palindrome obj=new Palindrome();
		obj.palindrome(str);
		obj.palindrome("radar");

	}

}
