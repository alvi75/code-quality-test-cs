public override BytesRef Next(){
    termUpto++;
    if (termUpto >= info.terms.Length){
        return null;
    }
    else{
        info.terms.Get(info.sortedTermUpto[termUpto], br);
        return br;
    }
}