public override string OutputToString(object output){
    if (!(output is IList<T> outputList)){
        outputList = (IList<T>)output;
        StringBuilder b = new StringBuilder();
        b.Append('[');
        for (int i = 0;
        i < outputList.Count;
        i++){
            if (i > 0){
                b.Append(", ");
            }
            b.Append(outputs.OutputToString(outputList[i]));
        }
        b.Append(']');
        return b.ToString();
    }