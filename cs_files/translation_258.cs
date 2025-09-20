public virtual string GetPath(string name, string dflt){
    string[] paths = new string[paths.Length + 1];
    System.Array.Copy(paths, 0, paths, 1, paths.Length);
    paths[0] = dflt;
    return Getenv();
}