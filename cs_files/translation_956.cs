public virtual void ClearDFA(){
    bool merged = false;
    List<DFAState> states = new List<DFAState>();
    List<DFAState> pending = new List<DFAState>();
    pending.Add(m_initial);
    while (pending.Count != 0){
        if (merged){
            states.AddRange(pending);
        }
    }
    merged = true;
    pending.Clear();
    foreach (DFAState s in pending){
        states.Add(s);
    }
}
m_states = states.ToArray();
}