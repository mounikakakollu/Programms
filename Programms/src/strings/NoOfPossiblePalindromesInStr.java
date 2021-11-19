/**
 * 
 */
package strings;

/**Count all the possible palindromes in the given string
 * 
 * @author mkakollu
 * 
 * For each letter in the i/p str, expanding left & right while checking for even and odd lenght palindromes. Move 
 * to next letter if it is palindrome.
 *
 */
public class NoOfPossiblePalindromesInStr {
	
	public int countPalindromes(String str, int i, int j) {
		int count = 0;
		while(i>=0 && j<str.length()) {
			if(str.charAt(i) != str.charAt(j))
				break;
			System.out.println(str.substring(i, j+1));
			count+=1;
			j+=1;
			i-=1;
		}
		return count;
	}

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		String str = "aabbbaa";
		int count=0;
		NoOfPossiblePalindromesInStr obj = new NoOfPossiblePalindromesInStr();
		for(int i=0; i<str.length(); i++) {
			count+=obj.countPalindromes(str, i-1, i+1);
			count+=obj.countPalindromes(str, i, i+1);
		}
		System.out.println("Total number of palindromes in the given string " + str + " are : " + count);

	}

}
