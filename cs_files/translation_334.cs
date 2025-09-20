public override ICollection<IP> Evaluate(IP){
    return Trees.FindAllToken(nts, ruleIndex);
}