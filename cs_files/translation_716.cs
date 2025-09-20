public virtual GroupGroupingSearch DisableCaching(){
    this.maxCacheRAMMB = null;
    this.maxToCache = null;
    return this;
}