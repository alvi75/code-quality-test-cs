public override TokenStream Create(TokenStream input){
    return new GermanMinimalStemFilterStream(input);
}