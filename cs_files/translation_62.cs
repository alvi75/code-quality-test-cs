public virtual bool remove(object o){
    lock (mutex){
        return c.remove(o);
    }
}