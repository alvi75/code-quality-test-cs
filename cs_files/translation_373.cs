public virtual void SetReadonly(bool readonly){
    if ((this.readonly & ~ALLOW_READER) != 0){
        throw new InvalidOperationException("can't alter readonly IntervalSet");
    }
    this.readonly = readonly;
}