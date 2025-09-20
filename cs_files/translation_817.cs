public virtual bool Get(string name, bool dflt){
    bool[] vals;
    object temp;
    if (valByRound.TryGetValue(name, out vals)){
        if (vals != null){
            return vals[roundNumber % vals.Length];
        }
    }