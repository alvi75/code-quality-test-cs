public virtual void SetTimeout(int millis){
    if (millis < 0){
        throw new ArgumentException(MessageFormat.Format(JGitText.Get().invalidTimeout, Sharpen.Extensions.ValueOf(millis)));
    }
    else{
        timeout = millis;
    }
}