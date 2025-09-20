public override bool Equals(object obj){
    if (this == obj){
        return true;
    }
    if (obj == null){
        return false;
    }
    if (GetType() != obj.GetType()){
        return false;
    }
    Toffs other = (Toffs)obj;
    if (StartOffset != other.StartOffset){
        return false;
    }
    if (EndOffset != other.EndOffset){
        return false;
    }
    return true;
}