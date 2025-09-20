public override bool Equals(object obj){
    if (this == obj){
        return true;
    }
    if (!(obj is AutomatonQuery)){
        return false;
    }
    var other = (AutomatonQuery)obj;
    if (GetType() != obj.GetType()){
        return false;
    }
    AutomatonQuery other2 = (AutomatonQuery)obj;
    if (Term == null){
        if (other2.Term != null){
            return false;
        }
    }
}
else if (!Term.Equals(other2.Term)){
    return false;
}
return true;
}