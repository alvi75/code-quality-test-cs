public override TokenStream Create(TokenStream input){
    return new RussianLightStemFilterStemmer(input);
}