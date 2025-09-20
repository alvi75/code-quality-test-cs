public override long Skip(long n){
    int s = (int)Math.Min(Available(), Math.Max(0, n));
    ptr += s;
    return s;
}