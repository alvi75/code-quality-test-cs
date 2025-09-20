public override string ToString(){
    StringBuilder r = new StringBuilder();
    r.Append("BlameResult[");
    r.Append(GetNewPath());
    r.Append("]");
    return r.ToString();
}