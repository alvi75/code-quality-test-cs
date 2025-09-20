public virtual Antlr4.Runtime.Misc.Interval(s0 = s;
AtnState p = s;
IntervalSet nextTokens = NextTokens(s);
while (nextTokens.Contains(TokenConstants.EPSILON)) {
    p = NextToken(s);
    if (p == null) return null;
}
return nextTokens;
}