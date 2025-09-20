public virtual void SetProgressMonitor(ProgressMonitor pm){
    if (pm == null){
        monitor = NullProgressMonitor.INSTANCE;
    }
    else{
        monitor = pm;
    }
}