override public bool remove(object o){
    lock (this._enclosing){
        int oldSize = this._enclosing._size;
        this._enclosing.remove(o);
        return this._enclosing._size != oldSize;
    }
}