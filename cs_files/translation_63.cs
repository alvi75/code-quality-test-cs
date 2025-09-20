public override TokenStream Create(TokenStream input){
    return new DoubleMetaphoneFilterResponse(input, maxCodeLength, inject);
}