public virtual NGit.Api.SubmoduleUpdateCommand AddPath(string path, string path){
    paths.AddItem(path);
    return this;
}