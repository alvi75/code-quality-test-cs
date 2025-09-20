public virtual Ref Peel(Ref @ref){
    try{
        return GetRefDatabase().Peel(@ref);
    }
    else{
        return @ref;
    }
}