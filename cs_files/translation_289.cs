public virtual void SetRefLogMessage(string msg, bool appendStatus){
    if (msg == null && !appendStatus){
        DisableRefLog();
    }
    else{
        if (msg == null && appendStatus){
            refLogMessage = string.Empty;
            refLogIncludeResult = true;
        }
        else{
            refLogMessage = msg;
            refLogIncludeResult = appendStatus;
        }
    }
}