public virtual DiffCommand CompareTo(AnyObjectId other){
    return new DiffCommand(repo, this, other);
}