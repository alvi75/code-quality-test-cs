public virtual bool IsSuccessful(){
    if (mergeResult != null){
        return mergeResult.IsSuccessful;
    }
    else{
        if (rebaseResult != null){
            return rebaseResult.Status.IsSuccessful;
        }
        else{
            return true;
        }
    }
}
throw new InvalidOperationException("Missing return statement in function");
}