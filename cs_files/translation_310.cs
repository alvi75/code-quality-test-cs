public virtual bool IsExpected(int symbol){
    ATN atn = Atn;
    ParserRuleContext ctx = _ctx;
    var state = atn.states[State];
    IVocabulary vocabulary = parser != null ? parser.Vocabulary : Vocabulary.EmptyVocabulary;
    IRuleTransition rt = (IRuleTransition)state.Transition(0);
    IVocabularySet following = vocabulary.GetAltsForRuleTransition(rt);
    if (following.Contains(symbol)){
        return true;
    }
    if (!following.Contains(TokenConstants.EPSILON)){
        return false;
    }
    while (ctx != null && ctx.invokingState >= 0 && vocabulary.GetAltsForRuleTransition(rt).Contains(TokenConstants.EPSILON)){
        ATNState invokingState = atn.states[ctx.invokingState];
        rt = (IRuleTransition)invokingState.Transition(0);
        following = vocabulary.GetAltsForRuleTransition(rt);
    }
    else{
        if (following.Contains(TokenConstants.EPSILON) && symbol == TokenConstants.EOF){
            return true;
        }
        return false;
    }
}
}
if (following.Contains(TokenConstants.EPSILON) && symbol == TokenConstants.EOF){
    return true;
}
return false;
}