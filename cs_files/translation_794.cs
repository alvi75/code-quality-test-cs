public virtual int Stem(char[] s, int len){
    if (len > 4 && s[len - 1] == 's'){
        len--;
    }
    if (len > 5 && (EndsWith(s, len, "ene") || (EndsWith(s, len, "ane") && useNynorsk)){
        len = len - 3;
    }
    if (len > 4 && (EndsWith(s, len, "er") || EndsWith(s, len, "en") || EndsWith(s, len, "et")){
        len = len - 2;
    }
    if (len > 3){
        switch (s[len - 1]){
            case 'a':case 'e':case 'i':case 'o':case 'u':return len - 1;
        }
    }
    return len;
}