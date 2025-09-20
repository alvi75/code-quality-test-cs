public override TokenStream Create(TokenStream input){
    var commonGrams = new CommonGramsFilter(m_luceneMatchVersion, input, commonWords);
    return commonGrams;
}