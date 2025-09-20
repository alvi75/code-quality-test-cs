public static void WriteUnicodeStringFlagAndData(ILittleEndianOutput out1, String value){
    bool is16Bit = HasMultibyte(value);
    out1.WriteByte(is16Bit ? 0x01 : 0x00);
    if (is16Bit){
        PutUnicodeLE(value, out1);
    }
    ;
}
else{
    PutCompressedUnicode(value, out1);
}
}