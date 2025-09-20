public virtual char RequireChar(IDictionary<string, string> args = null, string name = null){
    string s;
    if (val == null || !val.Any()){
        throw new System.ArgumentException("Configuration Error: missing parameter '" + name + "'");
    }
    val = val[name];
    if (s.Length != 1){
        throw new System.ArgumentException("Illegal " + name + " parameter: length must be 1 (" + s.Length + " given): " + s);
    }
    return s[0];
}