public virtual int GetCells(){
    int size = 0;
    foreach (char c in cells.Keys){
        Cell e = At(c);
        if (e.cmd >= 0 || e.@ref >= 0){
            size++;
        }
    }
}
}