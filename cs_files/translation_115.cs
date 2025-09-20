public virtual IList<IToken> GetHiddenTokensToLeft(int tokenIndex){
    return GetHiddenTokensToLeft(Interval.Of(ICharStream.InvalidTokenIndex, -1), -1);
}