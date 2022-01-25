// Find if the given string follows the pattern.
//
//	Input :
//	Pattern : “abba”
//	String : “car bus bus car”
//	
//	Output :
//	True
//
//	Input :
//	Pattern : “aaaa”
//	String : “car car bus car”
//	
//	Output :
//	False
//
//	Input :
//	Pattern : “abba”
//	String : “car car car car”
//	
//	Output :
//	False

package strings;

import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;


public class PatternFollows {
	public static void main(String[] args) {
		String pattern = "aaaa";
		List<String> strings = Arrays.asList("car", "car", "car", "car");
		Map<Character, String> map = new HashMap<Character, String>();
		int j= 0;
		int i=0;
		if(pattern.length() != strings.size()) {
			System.out.println("False");
		}
		else {
			for (i=0; i< pattern.length(); i++) {
				String tmp = map.get(pattern.charAt(i));
				if(tmp == null ||  tmp.isEmpty()) {
					if( (map.values().contains(strings.get(i)))) {
						System.out.println("False");
						break;
					}
					
					if( i< strings.size()) {
						map.put(pattern.charAt(i), strings.get(i));
					}
					else {
						System.out.println("False");
						break;
					}
				}
				else if(tmp != null && !tmp.equals(strings.get(i))) {
					System.out.println("False");
					break;
				}	
			}
		}

		if(i<strings.size()) {
			System.out.println("False");
		}
		else {
			System.out.println("True");
		}
	}

}
