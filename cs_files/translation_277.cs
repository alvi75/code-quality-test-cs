public virtual NGit.Api.RenameBranchCommand SetOldName(string oldName){
    CheckCallable();
    this.oldName = oldName;
    return this;
}