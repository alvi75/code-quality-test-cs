public RevFlagSet(ICollection<RevFlag> s){
    flags = new JCG.HashSet<RevFlag>();
    foreach (RevFlag flag in s){
        flags.AddItem(flag);
    }
}