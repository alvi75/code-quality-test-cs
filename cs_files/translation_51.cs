public IList<CharsRef> UniqueStems(char[] word, int length){
    IList<CharsRef> stems = Stem(word, length);
    if (stems.Count < 2){
        return stems;
    }
    var terms = new JCG.HashSet<char[]>();
    IList<CharsRef> deduped = new List<CharsRef>();
    foreach (CharsRef s in stems){
        if (!terms.Contains(s)){
            deduped.Add(s);
            terms.Add(new char[s.Length]){
                for (int i = 0;
                i < s.Length;
                i++){
                    terms.Add(s[i]);
                }
            }
        }