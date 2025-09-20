public virtual IErrorNode AddErrorNode(IToken badToken){
    ErrorNodeImpl t = new ErrorNodeImpl(badToken);
    AddChild(t);
    t.Parent = this;
    return t;
}