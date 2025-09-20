public virtual void Add(string text, CharsRef input){
    int hash = MurmurHash2.HashFunction32(input);
    lock (this){
        if (hash < 0){
            hash = hash * -1;
        }
        if (pending[hash & 0x7FFF]){
            if (pending[hash & 0x7FFF].length == pending.Length){
                pending = ArrayUtil.Grow(pending, 1 + pending.Length);
            }
            pending[pending.Length++] = new PendingInput(hash, input);
        }
    }
    );
}