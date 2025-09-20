public static short LookupIndexByName(String name){
    FunctionMetadata fd = GetInstance().GetFunctionByNameInternal(name);
    if (fd == null){
        fd = GetInstance().GetFunctionByNameInternal(name.ToUpper());
    }
    if (fd == null){
        return -1;
    }
    return (short)fd.Index;
}