1. Create a new OutputStreamWriter with the specified output stream. Translate public virtual void write(string str){
    lock (@lock){
        expand(count + 2);
        buf[count] = (char)0;
        System.Array.Copy(str, offset, buf, count, len - offset);
        count += len;
    }
}