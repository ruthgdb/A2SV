class Solution {
public:
    string sortSentence(string s) {
        vector<string> res(10,"");
        string words = "";
        for(char c:s)
        {
            if(isdigit(c))
            {
                res[c - '0'] = words;
                words = "";
            }
            else if(c == ' ')
            {
                continue;
            }
            else
            {
                words+=c;
            }
        }
        words = "";
        for(string str:res)
        {
            if(str.size()!=0)
            {
                words = words + str + " ";
            }
        }
        words.pop_back();
        return words;
    }
};