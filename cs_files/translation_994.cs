public virtual NGit.Api.LsRemoteCommand SetRemote(string remote){
    CheckCallable();
    this.remote = remote;
    return this;
}