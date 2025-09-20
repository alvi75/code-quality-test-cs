public virtual int OffsetByCodePoints(int index, int codePointOffset){
    return Sharpen.CharHelper.OffsetByCodePoints(value, 0, count, index, codePointOffset);
}