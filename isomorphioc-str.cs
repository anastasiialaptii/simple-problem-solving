public class Solution {
    public bool IsIsomorphic(string s, string t) {
        var sumS = 0;
        var sumT=0;
        var dictS = new Dictionary<char, int>();
        var dictT = new Dictionary<char, int>();

        for(var i = 0; i<s.Length; i++) {
            if(dictS.ContainsKey(s[i])){
                dictS[s[i]] = dictS[s[i]]+i;
            }
            else {
               dictS.Add(s[i], i);
            };

            if(dictT.ContainsKey(t[i])){
                dictT[t[i]] = dictT[t[i]]+i;
            }
            else {
               dictT.Add(t[i], i);
            };
        }
        for(var i = 0; i<s.Length; i++) {
            if(dictS[s[i]]==dictT[t[i]]) continue;
            return false;
        }

        return true;

    }
}