0x01 : Protect Sheet1.Protect = (bool)(field_1_protect != 0);
if (frec.Field_2_password == 0){
    field_2_username = null;
}
else{
    field_2_username = StringUtil.ReadUnicodeString(frec.Field_4_username_len);
}
return recSize;
}