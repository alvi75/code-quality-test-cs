public virtual IToken EmitEOF(){
    IToken cpos = _input.LT(-1);
    int line = _input.Line;
    IToken eof = _factory.Create(Tuple.Create((ITokenSource)_input, _tokenFactorySourcePair), TokenConstants.EOF, null, TokenConstants.DefaultChannel, _input.Index, _input.Index - 1, line, cpos);
    Emit(eof);
    return eof;
}