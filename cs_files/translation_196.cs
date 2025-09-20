public virtual void SetMultiValued(string dimName, bool v){
    lock (this){
        if (!fieldTypes.TryGetValue(dimName, out DimConfig fieldType)){
            fieldTypes[dimName] = new DimConfig {
                MultiValued = v }
                ;
            }
            else{
                fieldType.IsMultiValued = v;
            }
        }
    }