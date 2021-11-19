package strings;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**You are given a dictionary of words and a large input string. 
 * You have to find out whether the input string can be completely segmented into the words of a given dictionary. 
 * The following two examples elaborate on the problem further.
 * given dic = {apple, pear, pier, pie} 
 * Input str = applepie => apple+pie(words in dic)
 * Input str = applepies => apple+pies(words not in dic)
 * @author mounika
 *
 */
public class StringSegmentation {
	
	public boolean checkForWords(List<String> dic, String word) {
		for(int i=0; i<word.length(); i++) {
			String  pre = word.substring(0, i);
			if(dic.contains(pre)) {
				String post = word.substring(i);
				if(!post.isEmpty() || dic.contains(post) || checkForWords(dic, post))
					return true;
			}
		}
		return false;
	}
	
	public static void main(String[] args) {
		StringSegmentation obj = new StringSegmentation();
		List<String> dic = Arrays.asList("hell", "hello", "on","now");
//				new ArrayList<String>(){"apple", "pear", "pier","pie"};
		String word = "hellonow";
		System.out.println(obj.checkForWords(dic, word));
	}

}
