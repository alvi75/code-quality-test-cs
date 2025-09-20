ublic static void Main(string[] args){
    bool printTree = false;
    string path = null;
    for (int i = 0;
    i < args.Length;
    i++){
        if (args[i].Equals("-printTree", StringComparison.Ordinal)){
            printTree = true;
        }
        else{
            path = args[i];
        }
        if (args.Length != (printTree ? 2 : 1)){
            throw new ArgumentException();
        }
    }
}
}