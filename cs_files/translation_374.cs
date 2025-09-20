public void ClearConsumingCell(FormulaCellCacheEntry cce){
    if (!_consumingCells.Contains(cce)){
        _consumingCells.Add(cce);
    }