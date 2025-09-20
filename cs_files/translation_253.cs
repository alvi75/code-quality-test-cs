public int ReadUShort(int count){
    int ch1;
    int ch2;
    try{
        ch1 = in1.ReadByte();
    }
    catch (IOException e){
        throw new RuntimeException(e);
    }
    else{
        if (ch1 == -1){
            return -1;
        }
    }
    ;
}
try{
    ch2 = in1.ReadByte();
}
catch (IOException e){
    throw new RuntimeException(e);
}
}
return (ch2 << 8) + (ch1 << 0);
}