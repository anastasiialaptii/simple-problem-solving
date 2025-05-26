public class Solution {
    public int RomanToInt(string s) {
        var dict = new Dictionary<char, int>() {
            {'I', 1},
            {'V', 5}, 
            {'X', 10}, 
            {'L', 50}, 
            {'C', 100}, 
            {'D', 500}, 
            {'M', 1000},
        };

        var sum=0;
        for(var i=0; i<s.Length; i++) { 

            sum+=dict[s[i]];

            if(i>0 && dict[s[i-1]]<dict[s[i]]) {
                sum-= dict[s[i-1]]*2;
            }

        }

        return sum;
    }
}