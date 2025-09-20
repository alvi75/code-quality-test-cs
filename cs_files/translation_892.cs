public override bool Equals(object o){
    if (!(o is State)){
        this.stateNumber == ((State)o).stateNumber && this.numberedTransitions.SequenceEqual(((State)o).numberedTransitions));
    }