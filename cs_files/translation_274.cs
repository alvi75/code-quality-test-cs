public java.io.BufferedReader(java.io.Reader @in, int size) : base(@in){
    if (size <= 0){
        throw new System.ArgumentException("size <= 0");
    }
    this.@in = @in;
    buf = new char[size];
}