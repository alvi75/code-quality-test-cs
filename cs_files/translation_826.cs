public QueryScorer(WeightedSpanTerm[] weightedTerms){
    termsToFind = new JCG.HashSet<string>();
    for(int i=0;
    i<weightedTerms.Length;
    i++){
        termsToFind.Add(weightedTerms[i].Term);
    }
}