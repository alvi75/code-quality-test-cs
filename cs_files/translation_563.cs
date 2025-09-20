public static FontCharset ValueOf(int value){
    if(value>=0&&value<=255)return _table[value];
}
return null;
}