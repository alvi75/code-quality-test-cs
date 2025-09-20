public override bool IncrementTokenAttribute(){
    if (used){
        return false;
    }
    ClearAttributes();
    termAttribute.Append(value);
    used = true;
    return true;
}