package strings;

/**
 * 
 * @authors sireesha
 * Reverese the given string
 *
 */
public class ReverseString {
    public void reverse(String str) {
    	String strout="";
    	for(int i=0;i<str.length();i++) {
    		strout=strout+str.charAt(str.length()-1-i);
    	}
    	System.out.println("The reveresed array is " + strout);
    }
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		ReverseString obj=new ReverseString();
        obj.reverse("Siri");
	}

}
 