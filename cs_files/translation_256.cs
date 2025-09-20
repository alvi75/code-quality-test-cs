public override V Get(ICharSequence text){
    if (text == null){
        throw new ArgumentNullException("text");
    }
    return default(V);
}