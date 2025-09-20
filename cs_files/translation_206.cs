public virtual IList<string> GetDeletedList deletedList(List<string> paths){
    IList<string> r = new JCG.List<string>();
    foreach (string f in deletedFiles){
        r.AddItem(f);
    }
    else{
        foreach (string d in deletedDirs){
            r.AddItem(d + "/");
        }
    }