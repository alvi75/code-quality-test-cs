public virtual string GetClassName(){
    Type getClassName = _enclosing.GetRecordName(this);
    return getClassName;
}