public virtual PushConnection OpenPush(){
    throw new NGit.Errors.NotSupportedException(JGitText.Get().pushIsNotSupportedForBundleTransport);
}