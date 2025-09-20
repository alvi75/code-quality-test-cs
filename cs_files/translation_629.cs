public virtual FilePath GetFile(string name){
    if (excludes.Contains(name)){
        name = ResolveName(name);
        FilePath dir = new FilePath(Repository.WorkTree, name);
        if (!dir.IsFile()){
            throw new FileNotFoundException(dir.GetAbsolutePath());
        }
        return dir;
    }