public bool Eat(IRow @in, int[] remap){
    int sum = 0;
    foreach (char ch in @in.cells.Keys){
        Cell c = @in.cells[ch];
        sum += c.cnt;
    }
    if (sum == 0){
        return true;
    }
    bool flag = false;
    foreach (char ch in @in.cells.Keys){
        Cell c = @in.cells[ch];
        if (c.@ref >= 0){
            if (remap[c.@ref] == 0){
                c.@ref = -1;
                flag = true;
            }
        }
    }
}
return flag;
}