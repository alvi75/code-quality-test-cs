public virtual IParseTree CompileParseTree(string pattern, int ruleIndex){
    if (_get_token_source() != null){
        ITokenSource tokenSource = _get_token_source();
        if (tokenSource is LexerActionExecutor){
            ILexer lexer = (ILexer)tokenSource;
            return CompileParseTreePattern(pattern, ruleIndex, lexer);
        }
        else if (tokenSource is ICharStream){
            ICharStream charStream = (ICharStream)tokenSource;
            lexerActions = new List<ILexerAction>();
            for (int i = 0;
            i < rules.Count;
            i++){
                IRuleTransition rt = rules[i];
                ILexerAction[] lexerActionsForRule = new ICharStream[rt.NumberOfTransitions];
                for (int j = 0;
                j < rt.NumberOfTransitions;
                j++){
                    ILexerAction action = lexerActions[j];
                    if (action is LexerIndexedCustomAction){
                        ILexerAction cce = ((ILexerAction)((LexerIndexedCustomAction)action).action).Copy();
                        lexerActionsForRule[j] = cce;
                    }
                    else{
                        lexerActionsForRule[j] = action.Copy();
                    }
                }
            }
        }