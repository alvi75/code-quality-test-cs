public override void reset(){
    lock (@lock){
        checkNotClosed();
        if (_mark == -1){
            throw new System.IO.IOException("Invalid mark");
        }
        pos = _mark;
    }
}