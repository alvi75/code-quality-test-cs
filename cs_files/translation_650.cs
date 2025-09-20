public virtual string GetFully(string key){
    StringBuilder result = new StringBuilder(tries.Count * 2);
    for (int i = 0;
    i < tries.Count;
    i++){
        string r = tries[i].GetFully(key);
        if (r == null || (r.Length == 1 && r[0] == EOM)){
            return result.ToString();
        }
        result.Append(r);
    }
    else{
        return null;
    }
}