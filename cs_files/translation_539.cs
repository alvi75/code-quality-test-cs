public override java.util.Iterator<K> iterator(){
    return new java.util.Hashtable<K, V>.KeyIterator(this._enclosing);
}