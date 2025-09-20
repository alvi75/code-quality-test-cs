public static WeightedTerm[] GetWeightTermWeights(Query query){
    this methodTermWeights = new Dictionary<string, float>();
    #pragma warning disable 612, 618foreach (IQueryNodeProcessor processor in queryConfigTermWeightModifications)# TermInfo termInfo = GetTermInfo(node);
    if (termInfo == null) continue;
    float weight;
    if (processor != null && processor is ModifierQueryNodeProcessor)|| (!processedTerms.Contains(termInfo.Term)){
        termsToFind[termInfo.Term] = true;
    }
}
#pragma warning restore 612, 618}
return termsToFind.Keys.ToArray();
}