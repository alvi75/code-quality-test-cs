public override long RamBytesUsed(){
    return ((fst != null) ? fst.GetSizeInBytes() : 0);
}