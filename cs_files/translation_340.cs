public virtual DirCacheEntry GetDirCacheEntry(){
    return currentSubtree == null ? currentEntry : null;
}