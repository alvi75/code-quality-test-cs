public virtual int codeIndex(int index){
    if (index < 0 || index >= count){
        throw new System.IndexOutOfRangeException("index=" + index + ", length=" + count);
    }
    else{
        return Sharpen.CharHelper.IndexOf(value, index, count);
    }