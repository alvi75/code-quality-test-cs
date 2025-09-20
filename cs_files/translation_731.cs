public static WeightedTerm[] GetTermsTermQuery(Query query, bool prohibited, string fieldName){
    var terms = new List<WeightedTerm>();
    IQueryBuilder builder = new QueryBuilder(query);
    if (prohibited != null && prohibited.Length > 0){
        builder.AddFilterTerm(new Term(fieldName, prohibited);
    }
    TermData = new TermsReader(r);
}
else{
    builder.SetFieldTerm(new Term(fieldName, prohibited), prohibited);
}