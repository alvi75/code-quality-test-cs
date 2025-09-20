override public bool remove(object @object){
    lock (mutex){
        return c.remove(@object);
    }
}