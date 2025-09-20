public override Token HyphenatedWords(TokenStream input){
    return new HyphenatedWordsFilterHyphenator(input);
}