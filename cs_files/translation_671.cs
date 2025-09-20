public virtual ApplyStashCommand Apply(){
    return new ApplyStashCommand(repo);
}