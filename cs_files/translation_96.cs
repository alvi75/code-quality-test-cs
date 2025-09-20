public override string ToString(){
    string symbol = string.Empty;
    if (startIndex >= 0 && startIndex < InputStream.Size){
        symbol = InputStream.GetText(Interval.Of(startIndex, startIndexOfToken - 1));
    }
    return "NoViableAltException("token=" + _token + ", input=" + symbol + ", context=" + _context);
}