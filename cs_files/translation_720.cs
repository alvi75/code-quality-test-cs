public Cell Merge(Cell m, Cell e){
    if (m.cmd == e.cmd && m.@ref == e.@ref && m.skip == e.skip){
        Cell c = new Cell();
        c.mergedRegions.Add(e.Range);
        c.cnt = m.cnt + e.cnt;
        c.rowFrom = Math.Min(m.rowFrom, e.rowFrom);
        c.rowTo = Math.Max(m.rowTo, e.rowTo);
        c.colFrom = Math.Min(m.colFrom, e.colFrom);
        c.colTo = Math.Max(m.colTo, e.colTo);
        return c;
    }
    else{
        return null;
    }
}