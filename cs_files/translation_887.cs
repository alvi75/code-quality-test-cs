public Record GetNext(){
    if (!HasNext()){
        throw new InvalidOperationException("Attempt to read past end of record stream");
    }
    _countRead++;
    return (Record)_list[_nextIndex++];
}