package arrays;
// First repeating element in the string

import java.util.Arrays;

public class FirstRepeatingElement {

  public char findFirstRepeatingElement(String sentence) {
    int[] count = new int[26];
    Arrays.fill(count, 0);
    for(int i=0; i<sentence.length(); i++) {
      int asci = (int) Character.toLowerCase(sentence.charAt(i));
      if(count[asci-97] == 0)
        count[asci-97] = 1;
      else
        return sentence.charAt(i);
    }
    return 0;

  }
  public static void main(String[] args) {
    FirstRepeatingElement obj = new FirstRepeatingElement();
    String word = "GeeksForGeeks";
    System.out.println(obj.findFirstRepeatingElement(word));
  }
}