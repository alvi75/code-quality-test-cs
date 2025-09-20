public virtual string GetPath(){
    string s = path.GetPath();
    if (s.Length == 0){
        return null;
    }
    if (s.IndexOf('/') != -1 && !s.StartsWith("/")){
        string[] elements = s.Split(new char[]{
            '/'}
        }
        );
        if (elements.Length == 0){
            return null;
        }
        string result = elements[elements.Length - 1];
        if (Constants.DOT_GIT.Equals(result, StringComparison.Ordinal)){
            result = elements[elements.Length - 2];
        }
        else{
            if (result.EndsWith(Constants.DOT_GIT_EXT, StringComparison.Ordinal)){
                result = Sharpen.Runtime.Substring(result, 0, result.Length - Constants.DOT_GIT_EXT.Length);
            }
        }
        return result;
    }
}
}
}