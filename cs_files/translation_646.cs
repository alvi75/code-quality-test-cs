public virtual void Recover(Recognizer recognizer, RecognitionException e){
    if (lastErrorIndex == recognizer.InputStream.Index && lastErrorState.StateNumber == recognizer.State){
        return;
    }
    LastErrorState = ((RuleContext)_input.LT(-1));
    ConsumeUntil(recogn);
}