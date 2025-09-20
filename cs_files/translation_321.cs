public override ObjectStream OpenStream(){
    ObjectStream @in = base.OpenStream();
    try{
        long sz = @in.GetSize();
        byte[] tmp = new byte[8192];
        long copied = 0;
        while (copied < sz){
            int n = @in.Read(tmp);
            if (n < 0){
                throw new EOFException();
            }
            @out.Write(tmp, 0, n);
            copied += n;
        }
        if (0 <= @in.Read()){
            throw new EOFException();
        }
    }
}
finally{
    @in.Close();
}
return @in;
}