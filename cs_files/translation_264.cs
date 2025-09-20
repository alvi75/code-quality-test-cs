public virtual IToken GetToken(ttype){
    IToken t = Jj_Looking_Ahead();
    int l = t.Type;
    if(t.Type == TokenConstants.EOF){
        throw new NotSupportedException("token of type " + ttype + " not available");
    }
    Jj_consume_token(ttype);
    return t;
}