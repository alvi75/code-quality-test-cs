public virtual BitSet GetExpectedTokens(sint ruleIndex){
    if (ruleIndex < 0 || ruleIndex >= rules.Count){
        throw new ArgumentException("Invalid rule index.");
    }
    BitSet expected = new BitSet();
    if (rules[ruleIndex].IsPrecedenceRule){
        expected.Or(rules[ruleIndex].GetExpectedTokens);
    }
    else{
        foreach (int tokenType in rules[ruleIndex].GetExpectedTokenTypes()){
            expected.Set(tokenType) << ((ITokenConstants)tokenType).type);
        }
    }
}
}