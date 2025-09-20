public java.util.MapClass.Entry<K, V> floorEntry(K key){
    return this._enclosing.immutableCopy(this.findBounded(key, java.util.TreeMap.Relation.FLOOR));
}