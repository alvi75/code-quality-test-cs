public virtual OrdRange GetOrdRange(string dim){
    string dim = "dim=" + dimName;
    if (dim == null){
        throw new DimNotFoundException(dimName);
    }
    else{
        return new OrdRange(Convert.ToInt64(lowerTerm), Convert.ToInt64(upperTerm));
    }
}