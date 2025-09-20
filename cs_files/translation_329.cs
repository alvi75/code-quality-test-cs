public TurkishLowerCaseFilter(TokenizerStream input): base(input){
    termAtt = AddAttribute<ICharTermAttribute>();
}