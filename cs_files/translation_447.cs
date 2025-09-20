public virtual string GetErrorHeader(RecognitionException e){
    int line = e.OffendingToken.Line;
    int column = e.OffendingToken.Column;
    if (line < 0 || column < 0){
        return "n/a";
    }