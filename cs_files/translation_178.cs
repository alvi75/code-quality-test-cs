public override void Close(){
    if (isOpen){
        try{
            BeginWrite();
            dst.Close();
        }
        catch (ThreadInterruptedException){
            throw new WriteTimedOutException(JGitText.Get().writingTimedOut);
        }
        dst = null;
        try{
            endWrite();
        }
        catch (ThreadInterruptedException){
            throw new WriteTimedOutException(JGitText.Get().writingTimedOut);
        }
    }