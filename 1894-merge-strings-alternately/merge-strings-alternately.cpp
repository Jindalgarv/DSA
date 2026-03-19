class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        int n1= word1.size();
        int n2= word2.size();
        int n= min(n1,n2);
        string s="";
        s.reserve(n1+n2);
        int k=0;
        for(int i=0;i<n;i++)
        {
            s.push_back(word1[i]);
            s.push_back(word2[i]);
            k++;
        }
        while(k<n1)
        {
            s.push_back(word1[k]);
            k++;
        }
        while(k<n2)
        {
            s.push_back(word2[k]);
            k++;
        }
        return s;
    }
};