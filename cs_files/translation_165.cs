public override TokenStream Create(TokenStream input){
    return new PortugueseStemFilterStemmerOverrideMap(input, exceptions);
}