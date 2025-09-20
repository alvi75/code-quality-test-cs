public virtual SubmoduleInitCommand AddPath(string path){
    if (initialized){
        throw new InvalidOperationException("submodule init has been called already");
    }
    paths.AddItem(path);
    return this;
}