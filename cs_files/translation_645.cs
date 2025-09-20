public virtual int Stem(char[] s, int len){
    int numVowels = NumVowels(s, len);
    for (int i = 0;
    i < m_affixes.Length;
    i++){
        Affix affix = m_affixes[i];
        if (numVowels > affix.m_vc && len >= affix.m_automata.Length + 3 && StemmerUtil.EndsWith(s, len, affix.m_suffix)){
            len = len - affix.m_suffix.Length;
        }
    }
}
return len;
}