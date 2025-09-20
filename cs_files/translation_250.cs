public virtual NGit.Api.RevertCommand Include(Ref commit){
    CheckCallable();
    commits.AddItem(commit);
    return this;
}