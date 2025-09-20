public SrndQuery PrimaryQuery(){
    SrndQuery q;
    switch ((jj_ntk == -1) ? Jj_ntk() : jj_ntk){
        case RegexpToken.LPAREN:Jj_consume_token(RegexpToken.LPAREN);
        q = FieldsQuery();
        Jj_consume_token(RegexpToken.RPAREN);
        break;
        case RegexpToken.OR:case RegexpToken.AND:case RegexpToken.W:case RegexpToken.N:q = PrefixQuery();
        break;
        case RegexpToken.TRUNCQUOTED:case RegexpToken.QUOTED:case RegexpToken.SUFFIXTERM:case RegexpToken.TERM:q = SimpleTermQuery();
        break;
        default:jj_la1[5] = jj_gen;
        Jj_consume_token(-1);
        throw new ParseException();
    }
    Jj_consume_token(RegexpToken.COMMA);
    q.Boost = GetDistanceValue(sourceField, q.Boost);
    return q;
}