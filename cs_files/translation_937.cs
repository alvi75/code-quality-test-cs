public virtual DirectoryReader GetIndexReader(){
    lock (this){
        if (indexReader != null){
            indexReader.IncRef();
        }
        return indexReader;
    }
}