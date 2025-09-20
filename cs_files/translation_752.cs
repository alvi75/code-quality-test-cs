public virtual IToken LT(int k){
    LazyInit();
    if (k == 0){
        return null;
    }
    if (k < 0){
        return Lb(-k);
    }
}
int i = p + k - 1;
if (i < 0){
    throw new ArgumentOutOfRangeException("token index " + k + " out of range 0.." + (tokens.Count - 1));
}
if (i >= tokens.Count){
    return null;
}
return tokens[i];
return tokens);
}