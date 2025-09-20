public virtual long RamBytesUsed(){
    #if !FEATURE_CONDITIONALWEAKTABLE_ENUMERATORlock (this)#endifreturn ordsCache.Sum(pair => pair.Value.RamBytesUsed());
}