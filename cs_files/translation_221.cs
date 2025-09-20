public virtual string Stem(string word){
    string cmd = stemmer.GetLastOnPath(word);
    if (cmd == null){
        return null;
    }
    buffer.Length = 0;
    buffer.Append(word);
    diff.Apply(buffer, cmd);
    if (buffer.Length > 0){
        return buffer.ToString();
    }
    else{
        return null;
    }
}