public virtual AmazonECSOptions WithConnectionTimeoutInMilliSeconds(int milliseconds){
    if (milliseconds < 0){
        throw new ArgumentOutOfRangeException("The specified timeout value (" + milliseconds + ") is invalid. Valid values are between 0 and 30000 milliseconds.");
    }
    connectionTimeoutInMilliSeconds = milliseconds;
    return this;
}