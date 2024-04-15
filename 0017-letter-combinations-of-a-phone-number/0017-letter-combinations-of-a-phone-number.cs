public class Solution {
    static IList<string> res = null;
        
        static int len = 0;
        static public void generateCombinations(string s, List<string> keys,int i)
        {
            if (s.Length == len)
            {
                res.Add(s);
                return;
            }
            string a=keys[i];
            if (s.Length == 0)
            {
                i++;
                foreach (char c in a)
                {
                    generateCombinations(c + "", keys,i);
                }
               
                
            }
            else
            {
                i++;
                foreach (char c in a)
                {
                    generateCombinations(s + c, keys,i);
                }
               
            }
        }
    public IList<string> LetterCombinations(string digits) {
        res = new List<string>();
                 len = digits.Length;
        if(len==0) return res;
            IDictionary<int, string> numberNames = new Dictionary<int, string>(){
    {2,"abc"},
    {3,"def"},
    {4,"ghi"},
    {5,"jkl"},
    {6,"mno"},
    {7,"pqrs"},
    {8,"tuv"},
    {9,"wxyz"}

};
        List<string> inputMapping = new List<string>();
                foreach (char c in digits)
                {
                    int idx = c - '0';
                    inputMapping.Add(numberNames[idx]);
                }
            generateCombinations("", inputMapping,0);
        return res;
        }
    
}