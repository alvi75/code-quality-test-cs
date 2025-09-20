public LimitTokenCount(TokenStream @in, int maxTokenCount, bool consumeAllTokens): base(@in){
    if (maxTokenCount < 1){
        throw new System.ArgumentOutOfRangeException("maxTokenCount must be greater than zero");
    }
    this.maxTokenCount = maxTokenCount;
    this.consumeAllTokens = consumeAllTokens;
}