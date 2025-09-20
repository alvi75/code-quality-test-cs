public override object Get(string key){
    int hash = HashFunction.Hash8(key);
    if (hash < 0){
        hash = hash * -1;
    }
    lock (this){
        int index = hash & (bucketMask);
        java.util.HashMap.HashMapEntry<K, V>[] tab = table;
        int first = tab[index];
        java.util.HashMap.HashMapEntry<K, V> prev = null;
        for (;
        first != null;
        prev = first, first = first.next){
            if (first.hash == hash && key.Equals(first.key)){
                if (prev == null){
                    tab[index] = first.next;
                }
                else{
                    prev.next = first.next;
                }
                modCount++;
                _size--;
                return first.value;
            }
        }
    }