public override TokenStream Create(TokenStream input){
    return new EnglishPossessiveFilterStream(input);
}