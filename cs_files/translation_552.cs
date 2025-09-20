public override int lastIndexOf(string subString, int start){
    lock (this){
        return base.lastIndexOf(subString, start);
    }
}