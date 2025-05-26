public class Solution {
    public IList<IList<int>> Generate(int numRows) {
       var res=new List<IList<int>>();
      res.Add([1]);
       if(numRows==1) return res;

        for(int i=0;i<numRows;i++) {
      
        var array = new int[i+1];

            for(int j = 0; j<=i; j++) {
                if(j==0){
                    array[j]=1;
                    continue;
                }

                if(j==i) {
                    array[j]=1; 
                    res.Add(array.ToList());
                    break;
                }

            array[j] = res[i-1][j-1] + res[i-1][j];
        }
      }

      return res;
    }
}