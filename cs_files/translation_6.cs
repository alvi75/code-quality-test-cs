public string GetFullMessage(){
    byte[] raw = buffer;
    int msgB = RawParseUtils.TagMessage(raw, 0);
    if (msgB < 0){
        return string.Empty;
    }
    System.Text.Encoding enc = RawParseUtils.ParseEncoding(raw);
    int msgE = RawParseUtils.EndOfParagraph(raw, msgB);
    string str = RawParseUtils.Decode(enc, raw, msgB, msgE);
    if (RevCommit.HasLF(raw, msgB, msgE)){
        str = str.Replace('\n', ' ');
    }
    else{
        str = str.Replace('\r', ' '));
    }
    return str;
}