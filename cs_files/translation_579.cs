public virtual bool Handles(string commandLine){
    return command.Length + 1 < commandLine.Length && commandLine[command.Length] == ' ' && commandLine.StartsWith(command, StringComparison.Ordinal);
}