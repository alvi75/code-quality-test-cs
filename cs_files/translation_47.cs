public override void Reset(){
    if (!First){
        ptr = 0;
    }
    if (!Eof){
        ParseEntry();
    }
}