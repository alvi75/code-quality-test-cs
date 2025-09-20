public IndonesianStemFilter(TokenStream input, bool stemDerivational): base(input){
    this.stemDerivational = stemDerivational;
    this.termAttr = AddAttribute<ICharTermAttribute>();
    this.keywordAttr = AddAttribute<IKeywordAttribute>();
}