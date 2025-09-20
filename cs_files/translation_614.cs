public java.nio.CharBuffer decode(java.nio.ByteBuffer @buffer){
    try{
        return new java.nio.DecoderResultImpl(this, @buffer).decode();
    }
    catch (java.nio.charset.CharacterCodingException ex){
        throw new System.Exception(ex.Message, ex);
    }
}