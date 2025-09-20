public override int Read(byte[] buf, int off, int len){
    lock (this){
        if (buf == null){
            throw new System.ArgumentNullException("buffer == null");
        }
        java.util.Arrays.checkOffset(buf.Length, off, len);
        if (len == 0){
            return 0;
        }
        int copyLen = count - pos;
        if (copyLen > len){
            System.Array.Copy(this.buf, pos, buf, off, len);
            pos += len;
        }
        else{
            System.Array.Copy(this.buf, pos, buf, off, copyLen);
            pos += copyLen;
            return copyLen;
        }
    }
    ;
}