public ParseException(Token currentTokenVal,int[][] expectedTokenSequencesVal, string[] tokenVal): base(new Message(QueryParserValuedStrings.INVALID_SYNTAX, Initialize(currentTokenVal, expectedTokenSequencesVal, TokenManager.GetImageVal())), currentToken = currentTokenVal;
expectedTokenSequences = expectedTokenSequencesVal;
tokenImage = val;
}