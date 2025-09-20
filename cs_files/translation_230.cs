public virtual NGit.Api.RefUpdate AddCommand(ICollection<ReceiveCommand> cmd){
    commands.AddItemRange(cmd);
    return this;
}