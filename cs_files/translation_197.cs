public virtual int GetCellsVal(){
    int size = 0;
    foreach (char c in cells.Keys){
        Cell e = At(c);
        if (e.cmd >= 0){
            size++;
        }
    }
    Size += size;
}
return size;
}