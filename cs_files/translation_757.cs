public MessageWriter(){
    buf = new ByteArrayOutputStream();
    enc = new OutputStreamWriter(buf, Constants.CHARSET);
}