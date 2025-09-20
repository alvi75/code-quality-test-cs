public int sumSizedocuments(int fromIx, int ToIx){
    int result = 0;
    for (int i = fromIx;
    i < ToIx;
    i++){
        result += _ptgs[i].Size;
    }
    return result;
}