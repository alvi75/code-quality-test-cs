public override TokenStream Create(TokenStream input){
    return new ElisionFilter(articles, input);
}