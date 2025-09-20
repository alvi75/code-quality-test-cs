public override string ToString(){
    return "<phraseslop value='" + GetValueString() + "'>" + "\n"+ GetChild().ToString() + "\n</phraseslop>";
}
else{
    return "<matchNoTerms value='" + GetValueString() + "'/>";
}